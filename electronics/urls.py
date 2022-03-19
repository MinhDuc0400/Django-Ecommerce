from django.urls import path

from . import views

urlpatterns = [
    path('laptops/', views.ManageLaptopView.as_view(), name='manage_laptop'),
    path('laptops/add/', views.AddLaptopView.as_view(), name='add_laptop'),
    path('laptops/edit/<int:pk>', views.EditLaptopView.as_view(), name='edit_laptop'),
    path('laptops/delete/<int:pk>', views.deleteLaptop, name='delete_laptop'),
]
