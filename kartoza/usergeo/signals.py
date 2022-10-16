from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from .models import User_Activity
from datetime import datetime


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    new_activity = User_Activity(user_fk=user, log_time=datetime.now(), status="logged in")
    new_activity.save()
    print('user {} logged in through page {}' .format(user.username, request.META.get('HTTP_REFERER')))


@receiver(user_login_failed)
def log_user_login_failed(sender, request, user, **kwargs):
    new_activity = User_Activity(user_fk=user, log_time=datetime.now(), status="login failed")
    new_activity.save()
    print('user logged in failed')


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    new_activity = User_Activity(user_fk=user, log_time=datetime.now(), status="logged out")
    new_activity.save()
    print('user {} logged out through page {}'.format(user.username, request.META.get('HTTP_REFERER')))