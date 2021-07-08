from sys import path
from typing import Text
from django.shortcuts import render
from .ScriptImagesOCR import ORCModule
from django.http import HttpResponse
from django.template import loader
from imageOCR.forms import ImagesForm
from django.conf import settings
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            
            #file = form.imageFile 
            a = form.save()
            pathimg = str(settings.MEDIA_ROOT)+ '/' + str(a.imageFile)
            print(pathimg)
            OCR = ORCModule.ORCImages(pathimg)
            #form.clear()
            form = ImagesForm
            text = OCR.text
            imgFile = a.imageFile
            context = {'text' : text,
            'form': form,
            'imgFile': imgFile}
            return HttpResponse(template.render(context, request))

    else:
        form = ImagesForm 
        context = {'form': form}
    return HttpResponse(template.render(context, request))