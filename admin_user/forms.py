from django import forms
from .models import Mensaje

class Messages(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['asunto','mensaje']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write a Title'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write a Description'}),
        }