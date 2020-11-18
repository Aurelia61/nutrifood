from django.db import models

class Product(models.Model):
    name_product = models.CharField(max_length=200)


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name_ingredient = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
