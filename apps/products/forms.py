from django import forms
from .models import Product

# Product add form
class ProductAddForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ['name', 'description', 'price', 'quantity', 'visible']
        labels = {
            'name': 'Nazwa produktu',
            'description': 'Opis produktu',
            'price': 'Cena produktu',
            'quantity': 'Stan magazynowy',
            'visible': 'Produkt widoczny dla klienta',
        }

        attr = {'class': 'w-100 mb-2 d-flex align-items-center justify-content-center'}
        attr_smaller = {'class': 'w-50 mb-2 d-flex align-items-center justify-content-center'}

        widgets = {
            'name': forms.TextInput(attrs=attr),
            'description': forms.Textarea(attrs=attr),
            'price': forms.NumberInput(attrs=attr_smaller),
            'quantity': forms.NumberInput(attrs=attr_smaller),
            'visible': forms.CheckboxInput(),
        }

    # name = forms.CharField(label='Nazwa produktu', max_length=250, widget=forms.TextInput(attrs=attr))
    # description = forms.CharField(label='Opis', max_length=1500, widget=forms.Textarea(attrs=attr))
    # price = forms.IntegerField(label='Cena', min_value=0, required=True, widget=forms.NumberInput(attrs=attr_smaller))
    # quantity = forms.IntegerField(label='Ilość w magazynie', min_value=0, required=True, widget=forms.NumberInput(attrs=attr_smaller))
    # visible = forms.BooleanField(label='Czy widoczne?', required=True, widget=forms.CheckboxInput())
    # img = forms.FileField(label='Zdjęcie', max_length=25, required=True)