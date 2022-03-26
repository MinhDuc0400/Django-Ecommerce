from django import forms

from electronics.models import Electronic, ElectronicItem, Laptop, MobilePhone, Tivi
from django.utils.crypto import get_random_string

TYPE_CHOICES = (
    ("Dell", "Dell"),
    ("HP", "HP"),
    ("Acer", "Acer"),
    ("Asus", "Asus"),
    ("MSI", "MSI"),
    ("Samsung", "Samsung"),
    ("Apple", "Apple"),
    ("LG", "LG"),
)

TYPE_CHOICES_CONNECTOR = (
    ("HDMI", "HDMI"),
    ("USB", "USB"),
    ("Optical", "Optical"),
    ("VGA", "VGA"),
    ("AV/Composite", "AV/Composite"),
    ("S-Video", "S-Video"),
    ("Component", "Component"),
)


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'warranty', 'screenSize',
                  'manufacturer', 'ram', 'cpu', 'card']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.NumberInput(attrs={'class': 'form-control'}),
            'screenSize': forms.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'cpu': forms.TextInput(attrs={'class': 'form-control'}),
            'card': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class TiviForm(forms.ModelForm):

    class Meta:
        model = Tivi
        fields = ['name', 'warranty', 'screenSize',
                  'manufacturer', 'connector']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.NumberInput(attrs={'class': 'form-control'}),
            'screenSize': forms.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
            'connector': forms.Select(choices=TYPE_CHOICES_CONNECTOR, attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class MobilePhoneForm(forms.ModelForm):

    class Meta:
        model = MobilePhone
        fields = ['name', 'warranty', 'screenSize',
                  'manufacturer', 'ram', 'cpu', 'camera']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.NumberInput(attrs={'class': 'form-control'}),
            'screenSize': forms.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'cpu': forms.TextInput(attrs={'class': 'form-control'}),
            'camera': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class ElectronicItemFormAdd(forms.ModelForm):

    class Meta:
        model = ElectronicItem
        fields = ['barCode', 'price', 'discount', 'electronic', 'img']
        widgets = {
            'barCode': forms.TextInput(attrs={'class': 'form-control', 'readOnly': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'electronic': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['electronic'].empty_label = None
        self.fields['electronic'].queryset = Electronic.objects.filter(
            status=True)
        self.fields['barCode'].initial = get_random_string(length=14)


class ElectronicItemFormEdit(forms.ModelForm):

    class Meta:
        model = ElectronicItem
        fields = ['barCode', 'price', 'discount', 'img']
        widgets = {
            'barCode': forms.TextInput(attrs={'class': 'form-control', 'readOnly': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
