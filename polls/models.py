from django.db import models

# Create your models here.

class DataPoint(models.Model):
    x = models.IntegerField("X Value", default=0)
    y = models.IntegerField("Y Value", default=0)

