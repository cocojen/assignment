# from django.db import models
#
#
# # Create your models here.
# # Product Model
# class Product(models.Model):
#     CATEGORIES = (
#         ('food', 'Food'),
#         ('drink', 'Drink'),
#         ('snack', 'Snack'),
#     )
#
#     SIZES = (
#         ('small', 'Small'),
#         ('large', 'Large'),
#     )
#
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.CharField(max_length=10, choices=CATEGORIES)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     cost = models.DecimalField(max_digits=6, decimal_places=2)
#     name = models.CharField(max_length=100)
#     description = models.TextField(null=True)
#     barcode = models.CharField(max_length=20, unique=True)
#     expiration_date = models.DateField()
#     size = models.CharField(max_length=5, choices=SIZES)
