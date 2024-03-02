from django.db import models


class Profile(models.Model):
    pass


class Vote(models.Model):
    pass


class Product(models.Model):
    type = models.CharField(max_length=200)
    price = models.IntegerField()
    incart = models.BooleanField()
    infavorites = models.BooleanField()


class SpecialProduct(models.Model):
    features = models.ForeignKey(to=Product, on_delete=models.CASCADE)
