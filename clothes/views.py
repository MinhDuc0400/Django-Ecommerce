from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from clothes.forms import ClothesItemFormAdd, ClothesItemFormEdit, DressForm, JeanForm, SwimWearForm
from clothes.models import Clothes, ClothesItem, Jean, Dress, SwimWear
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.

class ManageJeanView(ListView):
    context_object_name = 'jeans'
    queryset = Jean.objects.all().filter(status=True)
    template_name = 'manages/clothes/manage_jean.html'

class AddJeanView(CreateView):
    form_class = JeanForm
    template_name = 'manages/clothes/add_edit.html'

class EditJeanView(UpdateView):
    model = Jean
    form_class = JeanForm
    template_name = 'manages/clothes/add_edit.html'

def deleteJean(request,pk):
    jean = Jean.objects.get(id=pk)
    jean.status = False
    jean.save()
    return redirect('manage_jean')

class ManageDressView(ListView):
    context_object_name = 'dresses'
    queryset = Dress.objects.all().filter(status=True)
    template_name = 'manages/clothes/manage_dress.html'

class AddDressView(CreateView):
    form_class = DressForm
    template_name = 'manages/clothes/add_edit.html'

class EditDressView(UpdateView):
    model = Dress
    form_class = DressForm
    template_name = 'manages/clothes/add_edit.html'

def deleteDress(request,pk):
    dress = Dress.objects.get(id=pk)
    dress.status = False
    dress.save()
    return redirect('manage_dress')


class ManageSwimWearView(ListView):
    context_object_name = 'swimwears'
    queryset = SwimWear.objects.all().filter(status=True)
    template_name = 'manages/clothes/manage_swimwear.html'

class AddSwimWearView(CreateView):
    form_class = SwimWearForm
    template_name = 'manages/clothes/add_edit.html'

class EditSwimWearView(UpdateView):
    model = SwimWear
    form_class = SwimWearForm
    template_name = 'manages/clothes/add_edit.html'

def deleteSwimWear(request,pk):
    swimwear = SwimWear.objects.get(id=pk)
    swimwear.status = False
    swimwear.save()
    return redirect('manage_swimwear')

class ManageItemView(ListView):
    context_object_name = 'clothesitems'
    queryset = ClothesItem.objects.all().filter(status=True)
    template_name = 'manages/clothes/manage_item.html'

class AddItemView(CreateView):
    form_class = ClothesItemFormAdd
    template_name = 'manages/clothes/add_item.html'

class EditItemView(UpdateView):
    model = ClothesItem
    form_class = ClothesItemFormEdit
    template_name = 'manages/clothes/add_item.html'

def deleteItem(request,pk):
    item = ClothesItem.objects.get(barCode=pk)
    item.status = False
    item.save()
    return redirect('manage_clothes_item')
