from pydoc import ModuleScanner
from unicodedata import name
from django.db import models
from numpy import size
from django.urls import reverse

# Create your models here.

class Clothes(models.Model):
    name = models.CharField(max_length=1000)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class SwimWear(Clothes):
    bustSize = models.IntegerField(default =0)
    waistSize = models.IntegerField(default =0)
    hipsSize = models.IntegerField(default =0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_swimwear")

class Jean(Clothes):
    pipe = models.CharField(max_length=5)
    size = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_jean")

class Dress(Clothes):
    size = models.CharField(max_length=255)
    lenght = models.CharField(max_length=255)
    pattern = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_dress")

class ClothesItem(models.Model):
    barCode = models.CharField(max_length=255, primary_key=True) 
    price = models.FloatField(default =0)
    discount = models.FloatField(default =0)
    clothes = models.OneToOneField(Clothes, on_delete=models.RESTRICT)
    img = models.ImageField(upload_to="clothes/")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.clothes.name

    def get_absolute_url(self):
        return reverse("manage_clothes_item")