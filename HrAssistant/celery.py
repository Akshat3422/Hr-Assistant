# HrAssistant/celery.py
# celery -A HrAssistant worker --pool=solo --loglevel=info  
# abobe command to run celery redis for background tasks 
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HrAssistant.settings')

app = Celery('HrAssistant')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()