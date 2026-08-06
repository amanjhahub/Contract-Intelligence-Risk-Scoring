from celery import Celery

celery_app = Celery(
    "contract_intelligence",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["tasks.contract_tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Kolkata",
    enable_utc=True,
)