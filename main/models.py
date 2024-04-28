from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=50)
    type = models.CharField("Вид", max_length=20)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание", max_length=100)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
