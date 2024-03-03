from django.db import models


class Profile(models.Model):
    pass


class Vote(models.Model):
    pass


class Type(models.Model):
    name = models.CharField(max_length=200)
    combining_types = models.JSONField()  # сочетающиеся товары
    not_combining_types = models.JSONField()  # несочетающиеся товары


class Cart(models.Model):
    products = models.ManyToManyField(to=Type)


class Favorites(models.Model):
    products = models.ManyToManyField(to=Type)


class ProductsStatus(models.Model):  # Статус товаров
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)  # пользователь
    cart = models.OneToOneField(to=Cart, on_delete=models.CASCADE)  # корзина
    favorites = models.OneToOneField(to=Favorites, on_delete=models.CASCADE)  # избранное


class Product(models.Model):
    type = models.ForeignKey(to=Type, on_delete=models.CASCADE)
    price = models.IntegerField()


class SpecialProduct(models.Model):
    features = models.ForeignKey(to=Product, on_delete=models.CASCADE)
