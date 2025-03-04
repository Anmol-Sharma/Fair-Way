from typing import Sequence, Any, Dict

import celery
from celery import Celery
from celery.signals import worker_process_init
import log_config
import logging
from utils.basic_utils import clean_file_content, aggregate_results, combined_results
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
def analyze_fair(metadata, file_type, user_tests=[]) -> Sequence[Dict[str, Any]]:
    """ """
    global model, fair_analyzer, splitter
    logger = logging.getLogger("celery")
    logger.info(f"Starting FAIR Analysis for Task:- {celery.current_task.request.id}")

    # Depending on the provided type of metadata, decide the next steps
    if isinstance(metadata, dict):
        # Online case
        # logger.info(metadata["api"]["metadata"])
        # logger.info(metadata["embedded"]["metadata"])
        pass

        # metadata = metadata["embedded"]["metadata"]
        # file_type = metadata["embedded"]["source"]

        # combined = combined_metadata(model, metadata=metadata)
        # file_type, metadata = combined["metadata_type"], combined["combined_metadata"]
        # logger.info("-" * 80)
        # logger.info(f"Combined Metadata Format:- {file_type}")
        # logger.info(f"Combined Metadata:- {metadata}")

    elif isinstance(metadata, str):
        # Local / Offline Case
        # Cleanup the file content for text files
        # if file_type and file_type == "text/plain":
        #     logger.info("Cleaning up plain text content before splitting.")
        #     metadata = clean_file_content(metadata)
        pass
    else:
        # Handle this case later on: Code should never be here
        pass

    # logger.info(f"Length of the final Metadata: {len(metadata)}")
    # file_type = file_type.lower()

    # Perform the split operations
    file_type_0 = metadata["api"]["source"]
    file_chunks_0 = splitter.split_file(
        metadata["api"]["source"],
        len(metadata["api"]["metadata"]),
        metadata["api"]["metadata"],
    )
    file_type_1 = metadata["embedded"]["source"]
    file_chunks_1 = splitter.split_file(
        metadata["embedded"]["source"],
        len(metadata["embedded"]["metadata"]),
        metadata["embedded"]["metadata"],
    )

    all_results = {"metrics": {}, "summary": {}}

    logger.info("Performing Domain-Agnostic Metrics")
    for m in fair_analyzer.all_domain_agnosticd_metrics:
        # For certain types of metrics use the full file content and not just chunks.
        # if file_type and file_type == "text/plain":
        #     logger.info("Cleaning up plain text content before splitting.")
        #     metadata = clean_file_content(metadata)
        #     file_chunks = splitter.split_file(file_type, len(metadata), metadata)
        # else:
        #     pass
        results = []
        for file_type, metadata, original_metadata in (
            (file_type_0, file_chunks_0, metadata["api"]["metadata"]),
            (file_type_1, file_chunks_1, metadata["embedded"]["metadata"]),
        ):
            logger.info(
                f"Performing analysis on metric: {m.metric_id} with file type: {file_type}"
            )
            file_chunks = metadata
            if m.metric_id in ("FsF_I3_01M"):
                logger.info("Performing test on whole file contents.")
                file_chunks = [
                    original_metadata,
                ]
            res = m.analyze_metric(
                model=model,
                file_chunks=file_chunks,
                file_type=file_type,
            )
            results.append(res)

        # Combine together the results using LLM
        combined_res = combined_results(model, results)
        all_results["metrics"][res["metric_id"]] = combined_res

    logger.info("Performing User-Defined Tests.")
    # if user_tests are defined, perform them else proceed forward
    if len(user_tests) > 0:
        vocab_tests = [t for t in user_tests if t["type"] == "Vocabulary Check"]
        standard_tests = [t for t in user_tests if t["type"] == "Standard Check"]

        if len(vocab_tests) > 0:
            v_m = U_Metric_Vocab(vocab_tests)
            v_res = v_m.analyze_metric(
                model=model,
                file_chunks=file_chunks,
                file_type=file_type,
            )
            all_results["metrics"][v_res["metric_id"]] = v_res

        if len(standard_tests) > 0:
            s_m = U_Metric_Standard(standard_tests)
            s_res = s_m.analyze_metric(
                model=model,
                file_chunks=file_chunks,
                file_type=file_type,
            )
            all_results["metrics"][s_res["metric_id"]] = s_res

    all_results["summary"] = aggregate_results(results=all_results["metrics"])
    all_results["summary"]["LLM"] = env_settings.llm_model.split(":")[0]
    return all_results
