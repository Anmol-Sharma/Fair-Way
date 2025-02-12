from typing import Sequence, Any, Dict

import celery
from celery import Celery
from celery.signals import worker_process_init
import log_config
import logging
from utils import clean_file_content, aggregate_results

from fair_analysis.model import ModelBase

from fair_analysis.fair_metrics.FsF_F1_01D.metric import M as M1
from fair_analysis.fair_metrics.FsF_F1_02D.metric import M as M2
from fair_analysis.fair_metrics.FsF_F2_01M.metric import M as M3
from fair_analysis.fair_metrics.FsF_F3_01M.metric import M as M4
from fair_analysis.fair_metrics.FsF_A1_01M.metric import M as M5
from fair_analysis.fair_metrics.FsF_I3_01M.metric import M as M6
from fair_analysis.fair_metrics.FsF_R1_01MD.metric import M as M7
from fair_analysis.fair_metrics.FsF_R1_1_01M.metric import M as M8

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

all_metrics = (M1, M2, M3, M4, M5, M6, M7, M8)
model = ModelBase(
    model_name=env_settings.llm_model,
    client_url=env_settings.ollama_url,
    options={
        "temperature": env_settings.temperature,
        "num_cts": env_settings.num_cts,
    },
)


@worker_process_init.connect
def setup_logging(sender=None, **kwargs):
    # Setup for each worker before its start some necessary settings and params
    # Setup logging
    log_config.setup_logging()
    # Use the global set of metrics and model
    global all_metrics, model


@cel.task(name="analyze", ignore_result=False)
def analyze_fair(file_type, file_content) -> Sequence[Dict[str, Any]]:
    """ """
    global all_metrics, model
    logger = logging.getLogger("celery")
    logger.info(f"Starting FAIR Analysis for Task:- {celery.current_task.request.id}")

    # Cleanup the file content
    file_content = clean_file_content(file_content)

    all_results = {"metrics": {}, "summary": {}}
    for m in all_metrics:
        res = m.analyze_metric(
            model=model,
            file_content=file_content,
            file_size=len(file_content),
            file_type=file_type,
        )
        all_results["metrics"][res["metric_id"]] = res

    all_results["summary"] = aggregate_results(results=all_results["metrics"])
    return all_results
