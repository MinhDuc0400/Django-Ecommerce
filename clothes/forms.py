from django import forms
from django.utils.crypto import get_random_string
from clothes.models import Clothes, ClothesItem, Dress, Jean, SwimWear 

TYPE_CHOICE = ( ("S","S"),
                ("M","M"),
                ("L","L"),
                ("XL","XL"),)

class JeanForm(forms.ModelForm):
    class Meta:
        model = Jean
        fields = ['name','color','material','pipe','size']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'material':forms.TextInput(attrs={'class':'form-control'}),
            'pipe':forms.TextInput(attrs={'class':'form-control'}),
            'size':forms.Select(choices=TYPE_CHOICE, attrs={'class':'form-control'}),
            
        }
    
    def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)
            # self.fields['category'].empty_label = None
            # self.fields['publisher'].empty_label = None
            # self.fields['authors'].empty_label = None
            # self.fields['publisher'].queryset = Publisher.objects.filter(status=True)
    
class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = ['name','color','material','size', 'lenght', 'pattern']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'material':forms.TextInput(attrs={'class':'form-control'}),
            'size':forms.Select(choices=TYPE_CHOICE, attrs={'class':'form-control'}),
            'lenght':forms.TextInput(attrs={'class':'form-control'}),
            'pattern':forms.TextInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)

class SwimWearForm(forms.ModelForm):
    class Meta:
        model = SwimWear
        fields = ['name','color','material','bustSize','waistSize', 'hipsSize']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'material':forms.TextInput(attrs={'class':'form-control'}),
            'bustSize':forms.NumberInput(attrs={'class':'form-control'}),
            'waistSize':forms.NumberInput(attrs={'class':'form-control'}),
            'hipsSize':forms.NumberInput(attrs={'class':'form-control'}),
            
        }
    
    def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)

class ClothesItemFormAdd(forms.ModelForm):
    class Meta:
        model = ClothesItem
        fields = ['barCode','price','discount','clothes', 'img']
        widgets = {
            'barCode':forms.TextInput(attrs={'class':'form-control', 'readOnly': True}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'discount':forms.NumberInput(attrs={'class':'form-control'}),
            'clothes':forms.Select(choices=TYPE_CHOICE, attrs={'class':'form-control'}),
            
        }
    
    def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)
            self.fields['clothes'].empty_label = None
            self.fields['clothes'].queryset = Clothes.objects.filter(status=True)
            self.fields['barCode'].initial = get_random_string(length=14)

class ClothesItemFormEdit(forms.ModelForm):
    class Meta:
        model = ClothesItem
        fields = ['barCode','price','discount','img']
        widgets = {
            'barCode':forms.TextInput(attrs={'class':'form-control', 'readOnly': True}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'discount':forms.NumberInput(attrs={'class':'form-control'}),
            
        }
    
    def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)