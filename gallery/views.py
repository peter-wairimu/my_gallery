from django.shortcuts import render,redirect
from .models import Category,Photo
# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)



    categories = Category.objects.all()
    return render(request,'my-gallery/gallery.html',{'categories': categories,'photos':photos})

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'my-gallery/photos.html',{'photo':photo})


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        img = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id =data['category'])
        elif data['new_category']!='':
            category, created = Category.objects.get_or_create(name=data['new_category'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            img = img

        )
        return redirect("gallery")
        




    return render(request,'my-gallery/form.html',{'categories': categories})
