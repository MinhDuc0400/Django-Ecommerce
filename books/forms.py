from django import forms
from .models import Author, Book, BookItem, Publisher
from django.utils.crypto import get_random_string
TYPE_CHOICES = (
    ("Lịch sử truyền thống", "Lịch sử truyền thống"),
    ("Kiến thức khoa học", "Kiến thức khoa học"),
    ("Văn học Việt Nam", 'Văn học Việt Nam'),
    ("Văn học nước ngoài", "Văn học nước ngoài"),
    ("Truyện tranh", "Truyện tranh")
)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','category','publisher','authors','pages','language','summary']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
            'publisher':forms.Select(attrs={'class':'form-control'}),
            'authors':forms.SelectMultiple(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'language':forms.TextInput(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)
            self.fields['category'].empty_label = None
            self.fields['publisher'].empty_label = None
            self.fields['authors'].empty_label = None
            # self.fields['publisher'].queryset = Publisher.objects.filter(status=True)
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','biography']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'biography': forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name','address']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }   
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs) 
class BookItemFormAdd(forms.ModelForm):
    class Meta:
        model = BookItem
        fields = ['barCode','price','discount','book','img']
        widgets = {
            'barCode':forms.TextInput(attrs={'class':'form-control','readOnly':True}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'discount':forms.NumberInput(attrs={'class':'form-control'}),
            'book':forms.Select(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)
            self.fields['book'].empty_label = None
            self.fields['book'].queryset = Book.objects.filter(status=True)
            self.fields['barCode'].initial = get_random_string(length=14)   
class BookItemFormEdit(forms.ModelForm):
    class Meta:
        model = BookItem
        fields = ['barCode','price','discount','img']
        widgets = {
            'barCode':forms.TextInput(attrs={'class':'form-control','readOnly':True}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'discount':forms.NumberInput(attrs={'class':'form-control'}),
        }
    