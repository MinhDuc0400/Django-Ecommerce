from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import redirect, render
from electronics.forms import LaptopForm

from electronics.models import Laptop

# Create your views here.


class ManageLaptopView(ListView):
    context_object_name = 'laptops'
    queryset = Laptop.objects.all().filter(status=True)
    template_name = 'manages/electronics/manage_laptop.html'


class AddLaptopView(CreateView):
    form_class = LaptopForm
    template_name = 'manages/electronics/add_edit.html'


class EditLaptopView(UpdateView):
    model = Laptop
    form_class = LaptopForm
    template_name = 'manages/electronics/add_edit.html'


def deleteLaptop(request, pk):
    laptop = Laptop.objects.get(id=pk)
    laptop.status = False
    laptop.save()
    return redirect('manage_laptop')
