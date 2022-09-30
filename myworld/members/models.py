from django.db import models


# Create your models here.
class Products(models.Model):
    # desc = models.CharField(max_length=300, default='')
    Title = models.TextField(max_length=300)
    Description = models.TextField(max_length=300, default='')
    Price = models.TextChoices('Price', '100,50,20')
    Summary = models.TextField(max_length=300, default="This is so cool!")
    Price_Selection = models.CharField(blank=True, choices=Price.choices, max_length=10)


class Cart(models.Model):
    Product = models.ForeignKey(Products, on_delete=models.PROTECT)


class Shirt(models.Model):
    SHIRT_SIZE = (
        ('S', 'SMALL'),
        ('M', 'MEDIUM'),
        ('L', 'LARGE')
    )
    name = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
