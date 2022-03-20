from django import forms


from django.utils.crypto import get_random_string

from shoes.models import Boots, HighHeels,  Shoes, ShoesItem, Sneaker

TYPE_CHOICES = (
    ("True", " Shoeslace"),
    ("Fales", "Khong Shoeslace"),

)

TYPE_CHOICES_CONNECTOR = (
    ("Dinh tan", "dinh tan "),
    ("khong Dinh tan ", "khong Dinh tan"),
    ("Optical", "Optical"),
    ("VGA", "VGA"),
    ("AV/Composite", "AV/Composite"),
    ("S-Video", "S-Video"),
    ("Component", "Component"),
)
TYPE_CHOICES_SIZE = (
    ("SM", "SM"),
    ("SL", "SL"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("LG", "LG"),

)


class BootsForm(forms.ModelForm):
    class Meta:
        model = Boots
        fields = ['name', 'size', 'color',
                  'material', 'style', 'isShoeslace']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'style': forms.NumberInput(attrs={'class': 'form-control'}),
            'isShoeslace': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class SneakerForm(forms.ModelForm):

    class Meta:
        model = Sneaker
        fields = ['name', 'size', 'color',
                  'material', 'style', 'clinch', 'sole']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'style': forms.NumberInput(attrs={'class': 'form-control'}),
            'clinch': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
            'sole': forms.Select(choices=TYPE_CHOICES_CONNECTOR, attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class HighHeelsForm(forms.ModelForm):

    class Meta:
        model = HighHeels
        fields = ['name', 'size', 'color',
                  'material', 'style', 'height']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'style': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.Select(choices=TYPE_CHOICES_SIZE, attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class ShoesItemFormAdd(forms.ModelForm):

    class Meta:
        model = ShoesItem
        fields = ['barCode', 'price', 'discount', 'shoes', 'img']
        widgets = {
            'barCode': forms.TextInput(attrs={'class': 'form-control', 'readOnly': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'shoes': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['shoes'].empty_label = None
        self.fields['shoes'].queryset = Shoes.objects.filter(
            status=True)
        self.fields['barCode'].initial = get_random_string(length=14)


class ShoesItemFormEdit(forms.ModelForm):

    class Meta:
        model = ShoesItem
        fields = ['barCode', 'price', 'discount', 'img']
        widgets = {
            'barCode': forms.TextInput(attrs={'class': 'form-control', 'readOnly': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
