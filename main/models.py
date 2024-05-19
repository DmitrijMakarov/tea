from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=50)
    type = models.CharField("Вид", max_length=20)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание", max_length=100)
    photo = models.ImageField("Изображение", upload_to="templates/tea_image", default="", blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Favourites(models.Model):
    user_id = models.IntegerField("Айди_пользователя")
    product_id = models.IntegerField("Айди_продукта")

    class Meta:
        verbose_name = "Любимое"
        verbose_name_plural = "Любимое"

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=200)
    products = models.JSONField()  # список сочетающихся и несочетающихся товаров

class SpecialProduct(models.Model):
    features = models.ForeignKey(to=Product, on_delete=models.CASCADE)

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=5000)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, default=1)


