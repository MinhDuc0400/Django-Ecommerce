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
