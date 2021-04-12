# celery imports
from celery.decorators import task
from celery.utils.log import get_task_logger



# logger 
logger = get_task_logger(__name__)

# json pickle serializers
import jsonpickle 

# import time for duration
from time import sleep

# import User
from django.contrib.auth import get_user_model

# import models 
from ..models import Balance, Transaction


# scheduling tasks
from celery import Celery
from celery.schedules import crontab

app = Celery()

import random
def random_number():
    return random.randint(5,7)

random_number()

# account updater 
@task(name='Balance updater scheduler')
def balance_updater():
    ''' trade duration is most useful for how long the scheduler runs
        not just to calculate the single days interest 
    '''

    email = 'braidej2@gmail.com'
    capital =  1420
    percentage_increase =  380
    trade_duration = 14
    rand_number = random_number()
    User = get_user_model()

    '''user data -email'''
    email = User.objects.get(email=email)

    '''variables'''
    # interest
    principal = capital
    time = trade_duration

    # daily percentage rate
    daily_percentage_rate = percentage_increase / trade_duration / 100

    # amount invested daily 
    daily_invested_amount = daily_percentage_rate * capital 
    daily_invested_amount = daily_invested_amount + rand_number

    # calculate the total interest 
    # interest = principal * time * daily_percentage_rate

    # updating the data in the scheduler
    Balance.objects.create(
        user=email,
        amount=daily_invested_amount
    )

    # sending notification for each transactions
    

    # sleep
    # sleep(duration)
    

    # update amounts
    # return f'{daily_invested_amount} , total amount    {capital + interest}'
    logger.info('Updated the balance')
    return f'{daily_invested_amount}'

# balance_updater('braidej@gmail.com', 1420, 380, 14)
# balance_updater('braidej@gmail.com', 14220, 30, 100)