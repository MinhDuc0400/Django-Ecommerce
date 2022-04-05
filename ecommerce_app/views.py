from pyexpat import model
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.db.models import Func, F
from django.core.paginator import Paginator

from books.models import BookItem
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
