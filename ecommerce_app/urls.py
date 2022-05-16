"""ecommerce_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('manage/books/', include('books.urls')),
    path('manage/shoes/', include('shoes.urls')),
    path('manage/electronics/', include('electronics.urls')),
    path('manage/clothes/', include('clothes.urls')),
    path('category/electronics/', views.CategoryElectronicView.as_view(),
         name='category_electronics'),
    path('electronics/detail/<pk>', views.CategoryElectronicDetailView.as_view(),
         name='electronic_detail'),
    path('category/books/', views.CategoryBookView.as_view(), name='category_books'),
    path('books/detail/<pk>', views.CategoryBookDetailView.as_view(),
         name='book_detail'),
    path('category/shoes/', views.CategoryShoesView.as_view(),
         name='category_shoes'),
    path('shoes/detail/<pk>', views.CategoryShoesDetailView.as_view(),
         name='shoes_detail'),
    path('category/clothes/', views.CategoryClothesView.as_view(),
         name='category_clothes'),
    path('clothes/detail/<pk>', views.CategoryClothesDetailView.as_view(),
         name='clothes_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
