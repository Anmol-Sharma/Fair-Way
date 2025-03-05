from typing import Sequence, Any, Dict

import celery
from celery import Celery
from celery.signals import worker_process_init
import log_config
import logging
from utils.basic_utils import clean_file_content, aggregate_results
from fair_analysis.splitter import Splitter

from fair_analysis.model import ModelBase
from fair_analysis.fair_analyzer import Analyzer
from config import get_env_settings, get_global_settings

from fair_analysis.fair_metrics.User_Metric.metric import V_Metric as U_Metric_Vocab
from fair_analysis.fair_metrics.User_Metric.metric import S_Metric as U_Metric_Standard

env_settings = get_env_settings()
global_settings = get_global_settings()

cel = Celery("tasks")
cel.conf.update(
    broker_url=env_settings.broker_url,
    result_backend=env_settings.result_backend,
    worker_concurrency=env_settings.worker_concurrency,
    worker_prefetch_multiplier=env_settings.worker_prefetch_multiplier,
    timezone=env_settings.timezone,
    enable_utc=env_settings.enable_utc,
    task_track_started=env_settings.task_track_started,
    task_annotations={"tasks.add": {"rate_limit": env_settings.task_rate_limit_add}},
    broker_connection_retry_on_startup=env_settings.broker_connection_retry_on_startup,
    result_expires=env_settings.result_expires,
    task_acks_late=env_settings.task_acks_late,
    task_reject_on_worker_lost=env_settings.task_reject_on_worker_lost,
    task_time_limit=env_settings.task_time_limit,
    worker_max_memory_per_child=env_settings.worker_max_memory_per_child,
)
model = ModelBase(
    model_name=env_settings.llm_model,
    client_url=env_settings.ollama_url,
    options={
        "temperature": env_settings.temperature,
        "num_cts": env_settings.num_cts,
    },
)
fair_analyzer = None
splitter = None


@worker_process_init.connect
def initialize_worker(sender=None, **kwargs):
    # Setup for each worker before its start some necessary settings and params

    # Setup logging
    log_config.setup_logging()

    # Setup the necessary variables
    global model, fair_analyzer, splitter
    fair_analyzer = Analyzer()
    splitter = Splitter()


@cel.task(name="analyze", ignore_result=False)
def analyze_fair(metadata, user_tests=[]) -> Sequence[Dict[str, Any]]:
    """ """
    global model, fair_analyzer, splitter
    logger = logging.getLogger("celery")
    logger.info(f"Starting FAIR Analysis for Task:- {celery.current_task.request.id}")
    all_results = {"metrics": {}, "summary": {}}

    # Cleanup the file content for text files
    if "file" in metadata.keys():
        if metadata["file"]["source"] == "text/plain":
            logger.info("Cleaning up plain text content before splitting.")
            metadata["file"]["metadata"] = clean_file_content(
                metadata["file"]["metadata"]
            )

    # Perform split operation on each harvested metdata
    for k in metadata.keys():
        metadata[k]["metadata_chunks"] = splitter.split_file(
            metadata[k]["source"], len(metadata[k]["metadata"]), metadata[k]["metadata"]
        )

    logger.info("Performing Domain-Agnostic Metrics")
    for m in fair_analyzer.all_domain_agnosticd_metrics:
        logger.info(
            f"Performing analysis on metric: {m.metric_id} with file types: {[x["source"] for x in metadata.values()]}"
        )
        res = m.analyze_metric(
            model=model,
            metadata=metadata,
        )
        all_results["metrics"][res["metric_id"]] = res

    # if user_tests are defined, perform them else proceed forward
    if len(user_tests) > 0:
        logger.info("Performing User-Defined Tests.")
        vocab_tests = [t for t in user_tests if t["type"] == "Vocabulary Check"]
        standard_tests = [t for t in user_tests if t["type"] == "Standard Check"]

        if len(vocab_tests) > 0:
            v_m = U_Metric_Vocab(vocab_tests)
            v_res = v_m.analyze_metric(
                model=model,
                metadata=metadata,
            )
            all_results["metrics"][v_res["metric_id"]] = v_res

        if len(standard_tests) > 0:
            s_m = U_Metric_Standard(standard_tests)
            s_res = s_m.analyze_metric(
                model=model,
                metadata=metadata,
            )
            all_results["metrics"][s_res["metric_id"]] = s_res

    all_results["summary"] = aggregate_results(results=all_results["metrics"])
    all_results["summary"]["LLM"] = env_settings.llm_model.split(":")[0]
    return all_results
