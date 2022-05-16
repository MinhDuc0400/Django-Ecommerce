from pyexpat import model
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.db.models import Func, F
from django.core.paginator import Paginator

from books.models import BookItem, Publisher
from clothes.models import ClothesItem
from electronics.models import ElectronicItem, Laptop, MobilePhone, Tivi
from shoes.models import ShoesItem

# Create your views here.


class HomeView(ListView):
    context_object_name = 'bookItems'
    queryset = BookItem.objects.filter(status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['electronicsItems'] = ElectronicItem.objects.filter(
            status=True)
        context['shoesItems'] = ShoesItem.objects.filter(status=True)
        context['ShoesItems'] = ShoesItem.objects.filter(status=True)
        return context

    template_name = 'home.html'
class CategoryElectronicView(ListView):
    context_object_name = 'electronicItems'

    def get_queryset(self):
        electronicItems = ElectronicItem.objects.filter(status=True)
        _manufacturer = self.request.GET.get('manufacturer')
        _price = self.request.GET.get('price')
        _sort = self.request.GET.get('sort')
        _page = self.request.GET.get('page')
        if _manufacturer:
            electronicItems = electronicItems.filter(
                electronic__manufacturer=_manufacturer)
        if _price:
            if _price == 'duoi5tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__lt=5000000)
            elif _price == '5trden10tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=5000000, priceBought__lt=10000000)
            elif _price == '10trden15tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=10000000, priceBought__lt=15000000)
            elif _price == '15trden25tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=15000000, priceBought__lt=25000000)
            elif _price == 'tren25tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=25000000)
        if _sort:
            if _sort == 'low-to-high':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('priceBought')
            elif _sort == 'high-to-low':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('-priceBought')

        paginator = Paginator(electronicItems, 8)
        electronicItems = paginator.get_page(_page)

        return electronicItems

    template_name = 'category_electronic.html'


class CategoryElectronicDetailView(DetailView):
    model = ElectronicItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sameItems'] = ElectronicItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?')
        print(ElectronicItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?'))
        return context

    template_name = 'electronic_detail.html'


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
        context['publishers'] = Publisher.objects.filter(status=True)
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


class CategoryShoesView(ListView):
    context_object_name = 'ShoesItems'

    def get_queryset(self):
        ShoesItems = ShoesItem.objects.filter(status=True)
        
        _style = self.request.GET.get('style')
        _price = self.request.GET.get('price')
        _sort = self.request.GET.get('sort')
        _page = self.request.GET.get('page')

        if _style:
            ShoesItems = ShoesItems.filter(shoes__style=_style)

        if _price:
            if _price == 'duoi100000':
                ShoesItems = ShoesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__lt=100000)
            elif _price == '100000den200000':
                ShoesItems = ShoesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=100000, priceBought__lt=200000)
            elif _price == 'tren200000':
                ShoesItems = ShoesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('priceBought')
        if _sort:
            if _sort == 'low-to-high':
                ShoesItems = ShoesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('priceBought')         
            elif _sort == 'high-to-low':
                ShoesItems = ShoesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('-priceBought')

        paginator = Paginator(ShoesItems, 8)
        ShoesItems = paginator.get_page(_page)

        return ShoesItems

    template_name = 'category_Shoes.html'


class CategoryShoesDetailView(DetailView):
    model = ShoesItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sameItems'] = ShoesItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?')
        print(ShoesItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?'))
        return context

    template_name = 'Shoes_detail.html'

class CategoryClothesView(ListView):
    context_object_name = 'clothesItems'

    def get_queryset(self):
        clothesItems = ClothesItem.objects.filter(status=True)
        _price = self.request.GET.get('price')
        _sort = self.request.GET.get('sort')
        _page = self.request.GET.get('page')

        if _price:
            if _price == 'duoi100000':
                clothesItems = clothesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__lt=100000)
            elif _price == '100000den200000':
                clothesItems = clothesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=100000, priceBought__lt=200000)
            elif _price == 'tren200000':
                clothesItems = clothesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=200000)

        if _sort:
            if _sort == 'low-to-high':
                clothesItems = clothesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('priceBought')
            elif _sort == 'high-to-low':
                clothesItems = clothesItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('-priceBought')

        paginator = Paginator(clothesItems, 8)
        clothesItems = paginator.get_page(_page)

        return clothesItems

    template_name = 'category_clothes.html'

class CategoryClothesDetailView(DetailView):
    model = ClothesItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sameItems'] = ClothesItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?')
        print(ClothesItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?'))
        return context

    template_name = 'clothes_detail.html'
