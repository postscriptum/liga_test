from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproj.settings')

app = Celery('myproj', broker='pyamqp://guest@localhost//')

app.autodiscover_tasks()
