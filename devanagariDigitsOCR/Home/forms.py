from django.forms import ModelForm
from .models import OCRimage


class ImageForm(ModelForm):
    class Meta:
        model = OCRimage
        fields = ['imgFile']
