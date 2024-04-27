from django.db import models


class Profile(models.Model):
    pass


class Vote(models.Model):
    pass


class Type(models.Model):
    name = models.CharField(max_length=200)
    products = models.JSONField()  # список сочетающихся и несочетающихся товаров


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


class Reviews(models.Model):
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)

