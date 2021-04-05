from django.forms import ModelForm
from django import forms
from app.models import Saver

class FormSaver(ModelForm):
    class Meta:
        model = Saver
        field = '__all__'
        widgets = [
            'judul': forms.TextInput({'class':'form-control'}),
            'link': forms.TextInput({'class':'form-control'}),
            'kategori_id': forms.TextInput({'class':'form-control'}),
        ]