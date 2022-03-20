from django import forms


from django.utils.crypto import get_random_string

from shoes.models import Boots, HighHeels,  Shoes, ShoesItem, Sneaker

TYPE_CHOICES = (
    (True, "Shoeslace"),
    (False, "Không Shoeslace"),

)

TYPE_SIZE = (
    ("M", "M"),
    ("XL", "XL"),
    ("L", "L"),
    ("S", "S"),

)

TYPE_STYLE = (
    ("Trẻ em", "Trẻ em"),
    ("Thanh niên", "Thanh niên"),
    ("Người cao tuổi", "Người cao tuổi"),
    ("Phụ nữ mang thai", "Phụ nữ mang thai"),

)
class BootsForm(forms.ModelForm):
    class Meta:
        model = Boots
        fields = ['name', 'size', 'color',
                  'material', 'style', 'isShoeslace']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.Select(choices=TYPE_SIZE,attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'style': forms.Select(choices=TYPE_STYLE,attrs={'class': 'form-control'}),
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
            'size': forms.Select(choices=TYPE_SIZE,attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'style': forms.Select(choices=TYPE_STYLE,attrs={'class': 'form-control'}),
            'clinch': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
            'sole': forms.TextInput(attrs={'class': 'form-control'}),
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
            'size': forms.Select(choices=TYPE_SIZE,attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'style': forms.Select(choices=TYPE_STYLE,attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
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
