from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField('Category')
    image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

