from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import redirect, render
from shoes.forms import BootsForm, HighHeelsForm, ShoesItemFormAdd, ShoesItemFormEdit, SneakerForm

from shoes.models import Boots, HighHeels,  ShoesItem, Sneaker

# Create your views here.


class ManageBootsView(ListView):
    context_object_name = 'boots'
    queryset = Boots.objects.all().filter(status=True)
    template_name = 'manages/shoes/manage_shoes.html'


class AddBootsView(CreateView):
    form_class = BootsForm
    template_name = 'manages/shoes/add_edit.html'


class EditBootsView(UpdateView):
    model = Boots
    form_class = BootsForm
    template_name = 'manages/shoes/add_edit.html'


def deleteBoots(request, pk):
    shoes = Boots.objects.get(id=pk)
    shoes.status = False
    shoes.save()
    return redirect('manage_shoes')


class ManageSneakerView(ListView):
    context_object_name = 'sneakers'
    queryset = Sneaker.objects.all().filter(status=True)
    template_name = 'manages/shoes/manage_sneaker.html'


class AddSneakerView(CreateView):
    form_class = SneakerForm
    template_name = 'manages/shoes/add_edit.html'


class EditSneakerView(UpdateView):
    model = Sneaker
    form_class = SneakerForm
    template_name = 'manages/shoes/add_edit.html'


def deleteSneaker(request, pk):
    sneaker = Sneaker.objects.get(id=pk)
    sneaker.status = False
    sneaker.save()
    return redirect('manage_sneaker')


class ManageHighHeelsView(ListView):
    context_object_name = 'highheels'
    queryset = HighHeels.objects.all().filter(status=True)
    template_name = 'manages/shoes/manage_highheels.html'


class AddHighHeelsView(CreateView):
    form_class = HighHeelsForm
    template_name = 'manages/shoes/add_edit.html'


class EditHighHeelsView(UpdateView):
    model = HighHeels
    form_class = HighHeelsForm
    template_name = 'manages/shoes/add_edit.html'


def deleteHighHeels(request, pk):
    highHeels = HighHeels.objects.get(id=pk)
    highHeels.status = False
    highHeels.save()
    return redirect('manage_highheels')


class ManageShoesItemView(ListView):
    context_object_name = 'shoesitems'
    queryset = ShoesItem.objects.all().filter(status=True)
    template_name = 'manages/shoes/manage_shoes_item.html'


class AddShoesItemView(CreateView):
    form_class = ShoesItemFormAdd
    template_name = 'manages/shoes/add_edit_item.html'


class EditShoesItemView(UpdateView):
    model = ShoesItem
    form_class = ShoesItemFormEdit
    template_name = 'manages/shoes/add_edit_item.html'


def deleteShoesItem(request, pk):
    shoesItems = ShoesItem.objects.get(barCode=pk)
    shoesItems.status = False
    shoesItems.save()
    return redirect('manage_shoes_item')
