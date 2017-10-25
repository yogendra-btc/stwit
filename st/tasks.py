from .models import *
from celery.task.schedules import crontab
from celery.decorators import periodic_task,task
from celery.utils.log import get_task_logger
from django.db import transaction
from .data_scrapper import DataScrapper
from datetime import datetime

data_scrapper = DataScrapper()

@transaction.atomic
def delete_results():
    with transaction.atomic():
        try:
            Results.objects.filter(user_id=1).delete()
        except Exception as e:
            raise e

@transaction.atomic            
def save_results(result_data):
    with transaction.atomic():
        try:
            user = User.objects.get(id=1)
            keyword_id = Keyword.objects.get(id=1)
            domain_id = Domain.objects.get(id=2)
            for result in result_data:
                Results.objects.create(
                    user_id = user,
                    keyword_id = keyword_id,
                    domain_id = domain_id,
                    result_string = result.text,
                    datetime = datetime.now()
                )
        except Exception as e:
            raise e


@periodic_task(run_every=(crontab(minute='*/5')), name="scrap_task", ignore_result=True)
def scrap_task():
        result_data = data_scrapper.get_google_results()
        delete_results()
        save_results(result_data)
        return "SUCCESS"

