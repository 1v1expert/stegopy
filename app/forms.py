from django.forms import ModelForm
from django import forms
from app.models import Steganographic


class EncryptForm(ModelForm):
    original_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": "custom-file-input",
                                                                             "accept": "image/png, "
                                                                                       "image/jpeg, "
                                                                                       "image/bmp, "
                                                                                       "image/jpg"}))
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                        "placeholder": "Введите текст",
                                                        "rows": 3,
                                                        }))
    
    # widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': "Введите код подтверждения"}))

    class Meta:
        model = Steganographic
        fields = ['original_image', 'text']


class DecryptForm(ModelForm):
    stego_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": "custom-file-input",
                                                                          "accept": "image/png, "
                                                                                    "image/jpeg, "
                                                                                    "image/bmp, "
                                                                                    "image/jpg"}))
    key = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                        "placeholder": "Введите ключ",
                                                        }))
    
    # widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': "Введите код подтверждения"}))
    
    class Meta:
        model = Steganographic
        fields = ['stego_image', 'key']
