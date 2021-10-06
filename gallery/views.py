from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request,'my-gallery/gallery.html')

def viewPhoto(request,pk):
    return render(request,'my-gallery/photos.html')


def addPhoto(request):
    return render(request,'my-gallery/form.html')
