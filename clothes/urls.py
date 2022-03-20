from django.urls import path

from . import views

# app_name = 'books'

urlpatterns = [
    path('jeans/', views.ManageJeanView.as_view(), name='manage_jean'),
    path('jeans/add/', views.AddJeanView.as_view(), name='add_jean'),
    path('jeans/edit/<int:pk>', views.EditJeanView.as_view(), name='edit_jean'),
    path('jeans/delete/<int:pk>', views.deleteJean, name='delete_jean'),

    path('dresses/', views.ManageDressView.as_view(), name='manage_dress'),
    path('dresses/add/', views.AddDressView.as_view(), name='add_dress'),
    path('dresses/edit/<int:pk>', views.EditDressView.as_view(), name='edit_dress'),
    path('dresses/delete/<int:pk>', views.deleteDress, name='delete_dress'),

    path('swimwears/', views.ManageSwimWearView.as_view(), name='manage_swimwear'),
    path('swimwears/add/', views.AddSwimWearView.as_view(), name='add_swimwear'),
    path('swimwears/edit/<int:pk>', views.EditSwimWearView.as_view(), name='edit_swimwear'),
    path('swimwears/delete/<int:pk>', views.deleteSwimWear, name='delete_swimwear'),

    path('items/', views.ManageItemView.as_view(), name='manage_item'),
    path('items/add/', views.AddItemView.as_view(), name='add_item'),
    path('items/edit/<pk>', views.EditItemView.as_view(), name='edit_item'),
    path('items/delete/<pk>', views.deleteItem, name='delete_item'),
]