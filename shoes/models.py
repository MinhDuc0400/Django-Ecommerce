from django.db import models

from django.urls import reverse


class Shoes (models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Boots(Shoes):
    isShoeslace = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_boots")


class Sneaker(Shoes):
    clinch = models.BooleanField(default=True)
    sole = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_sneaker")


class HighHeels (Shoes):
    height = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_highheel")


class ShoesItem (models.Model):
    barCode = models.CharField(max_length=255, primary_key=True)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    shoes = models.OneToOneField(Shoes, on_delete=models.RESTRICT)
    img = models.ImageField(upload_to="shoes/")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.shoes.name

    def get_absolute_url(self):
        return reverse("manage_shoes_item")
# Create your models here.
