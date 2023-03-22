from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model= Message
        fields = ['text']
        labels = {
            'text': 'Tekst wiadomości',
        }

        attr = {'class': 'w-100 h-25 mb-2 d-flex align-items-center justify-content-start'}

        widgets = {
            'text': forms.Textarea(attrs=attr)
        }