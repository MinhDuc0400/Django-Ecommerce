from django import forms

from electronics.models import Laptop

TYPE_CHOICES = (
    ("Dell", "Dell"),
    ("HP", "HP"),
    ("Acer", 'Acer'),
    ("Asus", "Asus"),
    ("MSI", "MSI"),
    ("Samsung", "Samsung"),
    ("Apple", "Apple"),
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
