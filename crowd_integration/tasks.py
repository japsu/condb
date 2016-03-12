from __future__ import absolute_import

import logging

from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model

from .utils import create_user as _create_user, update_user as _update_user


logger = logging.getLogger('kompassi')


@shared_task(ignore_result=True)
def create_user(user_pk, password):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    _create_user(user, password)


@shared_task(ignore_result=True)
def update_user(user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    _update_user(user)