from django import forms
from django.forms import ModelForm
from .models import ImageForOCR

class ImagesForm(ModelForm):
    class Meta:
        model = ImageForOCR
        fields = ['imageFile',]
        widgets = {
            'imageFile': forms.ClearableFileInput(attrs={'id': 'document_attachment_doc'}),
        }