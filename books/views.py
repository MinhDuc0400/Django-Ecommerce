from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView

from books.forms import AuthorForm, BookForm,BookItemFormAdd, BookItemFormEdit, PublisherForm
from books.models import Author, Book, BookItem, Publisher

# Create your views here.

class ManageBookView(ListView):
    context_object_name = 'books'
    queryset = Book.objects.all().filter(status=True)
    template_name = 'manages/books/manage_book.html'

class AddBookView(CreateView):
    form_class = BookForm
    template_name = 'manages/books/add_edit.html'

class EditBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'manages/books/add_edit.html'

def deleteBook(request,pk):
    book =Book.objects.get(id=pk)
    book.status=False
    book.save()
    return redirect('manage_book')
class ManageAuthorView(ListView):
    context_object_name = 'authors'
    queryset = Author.objects.all().filter(status=True)
    template_name = 'manages/books/manage_author.html'

class AddAuthorView(CreateView):
    form_class = AuthorForm
    template_name = 'manages/books/add_edit.html'

class EditAuthorView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'manages/books/add_edit.html'

def deleteAuthor(request,pk):
    author=Author.objects.get(id=pk)
    author.status=False
    author.save()
    return redirect('manage_author')
class ManagePublisherView(ListView):
    context_object_name = 'publishers'
    queryset = Publisher.objects.all().filter(status=True)
    template_name = 'manages/books/manage_publisher.html'

class AddPublisherView(CreateView):
    form_class = PublisherForm
    template_name = 'manages/books/add_edit.html'

class EditPublisherView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'manages/books/add_edit.html'

def deletePublisher(request,pk):
    publisher=Publisher.objects.get(id=pk)
    publisher.status=False
    publisher.save()
    return redirect('manage_publisher')
class ManageItemView(ListView):
    context_object_name = 'items'
    queryset = BookItem.objects.all().filter(status=True)
    template_name = 'manages/books/manage_item.html'

class AddItemView(CreateView):
    form_class = BookItemFormAdd
    template_name = 'manages/books/add_edit_item.html'

class EditItemView(UpdateView):
    model = BookItem
    form_class = BookItemFormEdit
    template_name = 'manages/books/add_edit_item.html'

def deleteItem(request,pk):
    item =BookItem.objects.get(barCode=pk)
    item.status=False
    item.save()
    return redirect('manage_book_item')