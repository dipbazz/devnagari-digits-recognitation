from django.shortcuts import render
from django.views.generic.base import View
from .models import OCRimage
from .forms import ImageForm
from .digit_recognizer import recognize_digit
from .image_processing import readImage


class Index(View):
    template_name = 'Home/index.html'

    def get(self, request):
        form = ImageForm()
        return render(request, self.template_name, {"forms":form})

    def post(self, request):
        OCRimage.objects.all().delete()
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

        else:
            return render(request, self.template_name, {'forms': form})

        data = OCRimage.objects.all()

        # function that returns the predicted digit value
        output = False
        output = readImage(data[0])

        return render(request, self.template_name, {'forms': form, 'data': data, 'output': output})


