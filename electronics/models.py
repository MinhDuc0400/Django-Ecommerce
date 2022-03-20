from django.db import models
from django.urls import reverse

# Create your models here.


class Electronic(models.Model):
    name = models.CharField(max_length=255)
    warranty = models.IntegerField(default=2)
    screenSize = models.FloatField(default=0)
    manufacturer = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Tivi(Electronic):
    connector = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_tivi")


class Laptop(Electronic):
    ram = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    card = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_laptop")


class MobilePhone(Electronic):
    ram = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manage_mobile_phone")


class ElectronicItem(models.Model):
    barCode = models.CharField(max_length=255, primary_key=True)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    electronic = models.OneToOneField(Electronic, on_delete=models.RESTRICT)
    img = models.ImageField(upload_to="electronics/")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.electronic.name

    def get_absolute_url(self):
        return reverse("manage_electronic_item")
