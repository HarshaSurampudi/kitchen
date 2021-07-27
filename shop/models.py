from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=13)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    from_date = models.DateField()
    to_date = models.DateField()
    breakfast = models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()

class Schedule(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField()
    breakfast = models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()



