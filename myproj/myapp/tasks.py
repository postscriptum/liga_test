from __future__ import absolute_import, unicode_literals
from myproj.celery import app
from django.conf import settings
import os


@app.task
def save_data(data):
    filename = os.path.join(os.path.dirname(settings.BASE_DIR), 'save.json')
    with open(filename, 'w') as f:
        f.write(data)
