# # Celery settings
# from __future__ import absolute_import, unicode_literals
# from celery import Celery
# from django.conf import settings
# import os

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puddle.settings')

# app = Celery('puddle')

# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)