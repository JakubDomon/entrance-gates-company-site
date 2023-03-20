from django import forms
from .models import Product, MainCategory

# Product form
class ProductForm(forms.ModelForm):
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

        attr = {'class': 'w-100 mb-2 d-flex align-items-center justify-content-start'}
        attr_smaller = {'class': 'w-50 mb-2 d-flex align-items-center justify-content-center'}

        widgets = {
            'name': forms.TextInput(attrs=attr),
            'description': forms.Textarea(attrs=attr),
            'price': forms.NumberInput(attrs=attr_smaller),
            'quantity': forms.NumberInput(attrs=attr_smaller),
            'visible': forms.CheckboxInput(),
        }

# Product update form
# Override form to show objects name
class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj) -> str:
        return obj.name

class ProductUpdateForm(forms.ModelForm):

    maincategory = NameModelChoiceField(queryset=MainCategory.objects.all(), widget=forms.Select, empty_label=None)

    class Meta:
        model= Product
        fields = ['maincategory','name', 'description', 'price', 'quantity', 'visible']
        labels = {
            'maincategory': 'Kategoria produktu',
            'name': 'Nazwa produktu',
            'description': 'Opis produktu',
            'price': 'Cena produktu',
            'quantity': 'Stan magazynowy',
            'visible': 'Produkt widoczny dla klienta',
        }

        attr = {'class': 'w-100 mb-2 d-flex align-items-center justify-content-start'}
        attr_smaller = {'class': 'w-50 mb-2 d-flex align-items-center justify-content-center'}

        widgets = {
            'name': forms.TextInput(attrs=attr),
            'description': forms.Textarea(attrs=attr),
            'price': forms.NumberInput(attrs=attr_smaller),
            'quantity': forms.NumberInput(attrs=attr_smaller),
            'visible': forms.CheckboxInput(),
        }

# Category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model= MainCategory
        fields = ['name', 'description', 'visible']
        labels = {
            'name': 'Nazwa kategorii',
            'description': 'Opis kategorii',
            'visible': 'Kategoria widoczna dla klienta',
        }

        attr = {'class': 'w-100 mb-2 d-flex align-items-center justify-content-start'}

        widgets = {
            'name': forms.TextInput(attrs=attr),
            'description': forms.Textarea(attrs=attr),
            'visible': forms.CheckboxInput(),
        }