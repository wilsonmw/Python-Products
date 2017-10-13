from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    weight = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    category = models.CharField(max_length=50)

