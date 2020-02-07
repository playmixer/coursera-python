import os
import django
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursera_house.settings')
django.setup()


from coursera_house.core.tasks import smart_home_manager


app = Celery('coursera_house')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5, smart_home_manager.s(), name='Check Smart Home')