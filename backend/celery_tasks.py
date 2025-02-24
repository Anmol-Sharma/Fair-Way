from typing import Sequence, Any, Dict

import celery
from celery import Celery
from celery.signals import worker_process_init
import log_config
import logging
from utils import clean_file_content, aggregate_results

from fair_analysis.model import ModelBase
from fair_analysis.fair_analyzer import Analyzer
from config import get_env_settings, get_global_settings

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


@worker_process_init.connect
def initialize_worker(sender=None, **kwargs):
    # Setup for each worker before its start some necessary settings and params

    # Setup logging
    log_config.setup_logging()
    global model, fair_analyzer
    fair_analyzer = Analyzer()


@cel.task(name="analyze", ignore_result=False)
def analyze_fair(file_type, file_content, user_tests=[]) -> Sequence[Dict[str, Any]]:
    """ """
    global model, fair_analyzer
    logger = logging.getLogger("celery")
    logger.info(f"Starting FAIR Analysis for Task:- {celery.current_task.request.id}")

    # Cleanup the file content
    file_content = clean_file_content(file_content)

    all_results = {"metrics": {}, "summary": {}}

    for m in fair_analyzer.all_metrics:
        res = m.analyze_metric(
            model=model,
            file_content=file_content,
            file_size=len(file_content),
            file_type=file_type,
        )
        all_results["metrics"][res["metric_id"]] = res

    # if user_tests are defined, perform them else proceed forward
    # if len(user_tests) > 0:
    #     logger.info("Performing User-Defined Tests.")
    #     # if t["type"] == "Vocabulary Check":
    #     # elif t.type == "Standard Check":
    #     #     # TODO: Define the test object for the standard check
    #     #     pass
    #     m = U_Metric(user_tests)
    #     res = m.analyze_metric(
    #         model=model,
    #         file_content=file_content,
    #         file_size=len(file_content),
    #         file_type=file_type,
    #     )
    #     # TODO: Define here the id for user-metric and save
    #     all_results["metrics"][res["metric_id"]] = res

    # TODO: Aggregate here only on non-user metrics for now until scoring is defined on them.
    all_results["summary"] = aggregate_results(results=all_results["metrics"])
    return all_results
