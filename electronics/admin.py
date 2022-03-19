from django.contrib import admin

from electronics.models import Electronic, ElectronicItem, Laptop, MobilePhone, Tivi

# Register your models here.
admin.site.register(Electronic)
admin.site.register(Tivi)
admin.site.register(Laptop)
admin.site.register(MobilePhone)
admin.site.register(ElectronicItem)
