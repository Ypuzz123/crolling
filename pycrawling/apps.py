from django.apps import AppConfig
from pycrawling import take_crawling
#from .take_crawling import *


class PycrawlingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pycrawling'

    def ready(self):
        take_crawling.start_crawling()
