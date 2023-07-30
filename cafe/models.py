from django.contrib.auth.models import User
from django.db import models

from djangopj import settings


# Create your models here.
# Product Model
class Product(models.Model):
    CATEGORIES = (
        ('coffee', 'Coffee'),
        ('tea', 'Tea'),
        ('ade', 'Ade'),
    )

    SIZES = (
        ('small', 'Small'),
        ('large', 'Large'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORIES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    barcode = models.CharField(max_length=20, unique=True)
    expiration_date = models.DateField()
    size = models.CharField(max_length=5, choices=SIZES)
