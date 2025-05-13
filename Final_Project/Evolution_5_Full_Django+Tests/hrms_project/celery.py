
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hrms_project.settings")

app = Celery("hrms_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

app.conf.CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

app.conf.update(
    task_routes={
        'hrms.tasks.send_welcome_email': {'queue': 'email_queue'},
    },
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
    accept_content=['json'],
    timezone='UTC',
)