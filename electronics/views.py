from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import redirect, render
from electronics.forms import ElectronicItemFormAdd, ElectronicItemFormEdit, LaptopForm, MobilePhoneForm, TiviForm

from electronics.models import ElectronicItem, Laptop, MobilePhone, Tivi

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


class ManageTiviView(ListView):
    context_object_name = 'tivis'
    queryset = Tivi.objects.all().filter(status=True)
    template_name = 'manages/electronics/manage_tivi.html'


class AddTiviView(CreateView):
    form_class = TiviForm
    template_name = 'manages/electronics/add_edit.html'


class EditTiviView(UpdateView):
    model = Tivi
    form_class = TiviForm
    template_name = 'manages/electronics/add_edit.html'


def deleteTivi(request, pk):
    tivi = Tivi.objects.get(id=pk)
    tivi.status = False
    tivi.save()
    return redirect('manage_tivi')


class ManageMobilePhoneView(ListView):
    context_object_name = 'mobilephones'
    queryset = MobilePhone.objects.all().filter(status=True)
    template_name = 'manages/electronics/manage_mobile_phone.html'


class AddMobilePhoneView(CreateView):
    form_class = MobilePhoneForm
    template_name = 'manages/electronics/add_edit.html'


class EditMobilePhoneView(UpdateView):
    model = MobilePhone
    form_class = MobilePhoneForm
    template_name = 'manages/electronics/add_edit.html'


def deleteMobilePhone(request, pk):
    mobilePhone = MobilePhone.objects.get(id=pk)
    mobilePhone.status = False
    mobilePhone.save()
    return redirect('manage_mobile_phone')


class ManageElectronicItemView(ListView):
    context_object_name = 'electronicitems'
    queryset = ElectronicItem.objects.all().filter(status=True)
    template_name = 'manages/electronics/manage_electronic_item.html'


class AddElectronicItemView(CreateView):
    form_class = ElectronicItemFormAdd
    template_name = 'manages/electronics/add_edit_item.html'


class EditElectronicItemView(UpdateView):
    model = ElectronicItem
    form_class = ElectronicItemFormEdit
    template_name = 'manages/electronics/add_edit_item.html'


def deleteElectronicItem(request, pk):
    electronicItems = ElectronicItem.objects.get(barCode=pk)
    electronicItems.status = False
    electronicItems.save()
    return redirect('manage_electronic_item')
