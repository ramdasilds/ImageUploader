from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import ImageForm
from .models import Image


def ImageUploaderProject(request):
    if request.method =='POST':
        fm=ImageForm(request.POST , request.FILES)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Image Successfully Upload !! ')
            return HttpResponseRedirect('/')

    fm=ImageForm()
    img=Image.objects.all()
    return render(request, 'image.html',{'img':img ,'fm':fm})