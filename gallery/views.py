from django.shortcuts import render
from .models import Category,Photo
# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    return render(request,'my-gallery/gallery.html',{'categories': categories,'photos':photos})

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'my-gallery/photos.html',{'photo':photo})


def addPhoto(request):
    return render(request,'my-gallery/form.html')
