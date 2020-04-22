from django.forms import ModelForm
from django import forms
from app.models import Steganographic
# from catalog.choices import TYPES_SEARCH
# from catalog.models import FixedAttributeValue, UnFixedAttributeValue, Manufacturer


class UploadDataForm(ModelForm):
    original_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    text = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите текст"}))
        # widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': "Введите код подтверждения"}))

    class Meta:
        model = Steganographic
        fields = ['original_image', 'text']
