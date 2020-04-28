from django.forms import ModelForm
from django import forms
from app.models import Steganographic


class UploadDataForm(ModelForm):
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
