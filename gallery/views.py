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

def delete_event(request,pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return  redirect ("gallery")









    

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_articles = Photo.search_category(search_term)
        message = f"{search_term}"
        return render(request, 'my-gallery/search.html',{"message":message,"categories": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'my-gallery/search.html',{"message":message})

