from unicodedata import name
from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("manage_author")


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("manage_publisher")


class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT)
    authors = models.ManyToManyField(Author)
    pages = models.IntegerField()
    language = models.CharField(max_length=255)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("manage_book")

    # def save(self, *args, **kwargs):
    #     barCode = get_random_string(length=32)
    #     return super(BookItem, self).save(*args, **kwargs)
class BookItem(models.Model):
    barCode = models.CharField(max_length=255, primary_key=True)
    book = models.OneToOneField(Book, on_delete=models.RESTRICT)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    img = models.ImageField(upload_to="books/")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.book.title+" | "+str(self.price)+" | "+str(self.discount)

    def get_absolute_url(self):
        return reverse("manage_item")
