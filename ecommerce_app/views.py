from pyexpat import model
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.db.models import Func, F
from django.core.paginator import Paginator

from books.models import BookItem, Publisher
from clothes.models import ClothesItem
from electronics.models import ElectronicItem
from shoes.models import ShoesItem

# Create your views here.

class HomeView(ListView):
    context_object_name = 'bookItems'
    queryset = BookItem.objects.filter(status=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['electronicsItems']=ElectronicItem.objects.filter(status=True)
        context['shoesItems']=ShoesItem.objects.filter(status=True)
        context['clothesItems']=ClothesItem.objects.filter(status=True)
        return context
    
    template_name = 'home.html'
class CategoryBookView(ListView):
    context_object_name = 'bookItems'

    def get_queryset(self):
        bookItems = BookItem.objects.filter(status=True)
        _publisher = self.request.GET.get('publisher')
        _price = self.request.GET.get('price')
        _sort = self.request.GET.get('sort')
        _page = self.request.GET.get('page')
        if _publisher:
            bookItems = bookItems.filter(
                book__publisher__name=_publisher)
        if _price:
            if _price == 'duoi100':
                bookItems = bookItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__lt=100000)
            elif _price == '100den200':
                bookItems = bookItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=100000, priceBought__lte=200000)
            elif _price == 'tren200':
                bookItems = bookItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gt=200000)
        if _sort:
            if _sort == 'low-to-high':
                bookItems = bookItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('priceBought')
            elif _sort == 'high-to-low':
                bookItems = bookItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('-priceBought')

        paginator = Paginator(bookItems, 8)
        bookItems = paginator.get_page(_page)
        return bookItems
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers']=Publisher.objects.filter(status=True)
        return context
    template_name = 'category_book.html'
        


class CategoryBookDetailView(DetailView):
    model = BookItem
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sameBookItems'] = BookItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?')
        return context
    template_name = 'book_detail.html'
