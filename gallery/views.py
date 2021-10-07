from django.shortcuts import render
from .models import Category,Photo
# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    return render(request,'my-gallery/gallery.html',{'categories': categories})

def viewPhoto(request,pk):
    return render(request,'my-gallery/photos.html')


def addPhoto(request):
    return render(request,'my-gallery/form.html')
