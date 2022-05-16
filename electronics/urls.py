from django.urls import path

from . import views

urlpatterns = [
    path('laptops/', views.ManageLaptopView.as_view(), name='manage_laptop'),
    path('laptops/add/', views.AddLaptopView.as_view(), name='add_laptop'),
    path('laptops/edit/<int:pk>', views.EditLaptopView.as_view(), name='edit_laptop'),
    path('laptops/delete/<int:pk>', views.deleteLaptop, name='delete_laptop'),

    path('tivis/', views.ManageTiviView.as_view(), name='manage_tivi'),
    path('tivis/add/', views.AddTiviView.as_view(), name='add_tivi'),
    path('tivis/edit/<int:pk>', views.EditTiviView.as_view(), name='edit_tivi'),
    path('tivis/delete/<int:pk>', views.deleteTivi, name='delete_tivi'),

    path('mobilephones/', views.ManageMobilePhoneView.as_view(),
         name='manage_mobile_phone'),
    path('mobilephones/add/', views.AddMobilePhoneView.as_view(),
         name='add_mobile_phone'),
    path('mobilephones/edit/<int:pk>',
         views.EditMobilePhoneView.as_view(), name='edit_mobile_phone'),
    path('mobilephones/delete/<int:pk>',
         views.deleteMobilePhone, name='delete_mobile_phone'),

    path('items/', views.ManageElectronicItemView.as_view(),
         name='manage_electronic_item'),
    path('items/add/', views.AddElectronicItemView.as_view(),
         name='add_electronic_item'),
    path('items/edit/<pk>',
         views.EditElectronicItemView.as_view(), name='edit_electronic_item'),
    path('items/delete/<pk>', views.deleteElectronicItem,
         name='delete_electronic_item'),
]
