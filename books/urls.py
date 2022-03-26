from django.urls import path

from . import views


urlpatterns = [
    path('', views.ManageBookView.as_view(), name='manage_book'),
    path('add/', views.AddBookView.as_view(), name='add_book'),
    path('edit/<int:pk>', views.EditBookView.as_view(), name='edit_book'),
    path('delete/<int:pk>', views.deleteBook, name='delete_book'),
    #author
    path('authors', views.ManageAuthorView.as_view(), name='manage_author'),
    path('authors/add/', views.AddAuthorView.as_view(), name='add_author'),
    path('authors/edit/<int:pk>', views.EditAuthorView.as_view(), name='edit_author'),
    path('authors/delete/<int:pk>', views.deleteAuthor, name='delete_author'),
    #publisher
    path('publishers', views.ManagePublisherView.as_view(), name='manage_publisher'),
    path('publishers/add/', views.AddPublisherView.as_view(), name='add_publisher'),
    path('publishers/edit/<int:pk>', views.EditPublisherView.as_view(), name='edit_publisher'),
    path('publishers/delete/<int:pk>', views.deletePublisher, name='delete_publisher'),
    #item
    path('items', views.ManageItemView.as_view(), name='manage_book_item'),
    path('items/add/', views.AddItemView.as_view(), name='add_book_item'),
    path('items/edit/<pk>', views.EditItemView.as_view(), name='edit_book_item'),
    path('items/delete/<pk>', views.deleteItem, name='delete_book_item'),
]
