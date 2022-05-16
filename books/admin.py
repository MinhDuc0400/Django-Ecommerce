# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Book, Author, BookItem, Publisher

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(BookItem)
