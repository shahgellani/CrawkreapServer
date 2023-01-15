import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrawlreapServer.settings")
app = Celery("celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


# @app.on_after_configure.connect
# def add_periodic(task , task_name , **kwargs):
#     print("In add periodic")
#     app.add_periodic_task(10.0, task.s(), name=task_name)
#
#
# @app.task
# def test():
#     print("arg")

app.conf.beat_schedule = {
    "add-every-60-seconds": {
        "task": "email_parser",
        "schedule": 1.0,
        # 'args': (16, 16)
    },
    # "add-every-1-minute": {
    #     "task": "check_status_of_bots",
    #     "schedule": 5.0,
    #     # 'args': (16, 16)
    # },
}
