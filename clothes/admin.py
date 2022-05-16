from django.contrib import admin

from clothes.models import Clothes, ClothesItem, Dress, Jean, SwimWear

# Register your models here.

admin.site.register(Clothes)
admin.site.register(SwimWear)
admin.site.register(Jean)
admin.site.register(Dress)
admin.site.register(ClothesItem)
