from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
# from main.celery.tasks import balance_updater


# set the default Django settings module for the celery program 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptoland.settings')

app = Celery('cryptoland')

'''
using a string here means the worker doesn't have to serialize the conf. object to child processes
'''

app.config_from_object('django.conf:settings')
app.conf.broker_url = 'redis://localhost:6379'

# load task modules from all registered django app conf
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) 

@app.task(bind=True)
def debug_task(self):
    # print(f'request: {self.request}')
    print('REQUEST: {0!r}'.format(self.request))
