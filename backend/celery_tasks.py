from typing import Sequence, Any, Dict

import celery
from celery import Celery
from celery.signals import worker_process_init
import log_config
import logging
from utils import clean_file_content, aggregate_results
from fair_analysis.splitter import Splitter

from fair_analysis.model import ModelBase
from fair_analysis.fair_analyzer import Analyzer
from config import get_env_settings, get_global_settings

from fair_analysis.fair_metrics.User_Metric.metric import Metric as U_Metric_Vocab

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
def analyze_fair(file_type, file_content, user_tests=[]) -> Sequence[Dict[str, Any]]:
    """ """
    global model, fair_analyzer, splitter
    logger = logging.getLogger("celery")
    logger.info(f"Starting FAIR Analysis for Task:- {celery.current_task.request.id}")

    # Cleanup the file content for text files
    if file_type == "text/plain":
        logger.info("Cleaning up plain text content before splitting.")
        file_content = clean_file_content(file_content)

    logger.info(len(file_content))

    # Perform the split operations
    file_chunks = splitter.split_file(file_type, len(file_content), file_content)
    logger.info(f"Total Number of File Chunks: {len(file_chunks)}")

    all_results = {"metrics": {}, "summary": {}}

    logger.info("Performing Domain-Agnostic Metrics")
    for m in fair_analyzer.all_domain_agnosticd_metrics:
        res = m.analyze_metric(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        all_results["metrics"][res["metric_id"]] = res

    logger.info("Performing User-Defined Tests.")
    # if user_tests are defined, perform them else proceed forward
    if len(user_tests) > 0:
        vocab_tests = [t for t in user_tests if t["type"] == "Vocabulary Check"]
        # standard_tests = [t for t in user_tests if t["type"] == "Standard Check"]

        v_m = U_Metric_Vocab(vocab_tests)
        # s_m = U_Metric_Standard(standard_tests)

        v_res = v_m.analyze_metric(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        # s_res = s_m.analyze_metric(
        #     model=model,
        #     file_chunks=file_chunks,
        #     file_type=file_type,
        # )
        all_results["metrics"][v_res["metric_id"]] = v_res
        # all_results["metrics"][s_res["metric_id"]] = s_res

    # TODO: Aggregate here only on non-user metrics for now until scoring is defined on them.
    all_results["summary"] = aggregate_results(results=all_results["metrics"])
    return all_results
