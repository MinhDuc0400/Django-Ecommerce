from django.urls import path

from . import views

urlpatterns = [
    path('boots/', views.ManageBootsView.as_view(), name='manage_boots'),
    path('boots/add/', views.AddBootsView.as_view(), name='add_boots'),
    path('boots/edit/<int:pk>', views.EditBootsView.as_view(), name='edit_boots'),
    path('boots/delete/<int:pk>', views.deleteBoots, name='delete_boots'),

    path('sneaker/', views.ManageSneakerView.as_view(), name='manage_sneaker'),
    path('sneaker/add/', views.AddSneakerView.as_view(), name='add_sneaker'),
    path('sneaker/edit/<int:pk>',
         views.EditSneakerView.as_view(), name='edit_sneaker'),
    path('sneaker/delete/<int:pk>', views.deleteSneaker, name='delete_sneaker'),

    path('highheels/', views.ManageHighHeelsView.as_view(),
         name='manage_highheels'),
    path('highheels/add/', views.AddHighHeelsView.as_view(),
         name='add_highheels'),
    path('highheels/edit/<int:pk>',
         views.EditHighHeelsView.as_view(), name='edit_highheels'),
    path('highheels/delete/<int:pk>',
         views.deleteHighHeels, name='delete_highheels'),

    path('item/', views.ManageShoesItemView.as_view(),
         name='manage_shoes_item'),
    path('item/add/', views.AddShoesItemView.as_view(),
         name='add_shoes_item'),
    path('item/edit/<pk>',
         views.EditShoesItemView.as_view(), name='edit_shoes_item'),
    path('item/delete/<pk>', views.deleteShoesItem, name='delete_shoes_item'),
]
