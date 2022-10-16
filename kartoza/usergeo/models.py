from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_Activity(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    log_time = models.DateTimeField(max_length=250)
    status = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user_fk.first_name} {self.user_fk.last_name}"


class User_Info(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    def first_name(self):
        return f"{self.user_fk.first_name}"

    def last_name(self):
        return f"{self.user_fk.last_name}"

    def __str__(self):
        return f"{self.user_fk.first_name} {self.user_fk.last_name}"



