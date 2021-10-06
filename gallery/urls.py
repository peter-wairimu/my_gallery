from django.urls import url
from .import views


urlpatterns=[

    url(r'^$',views.gallery, name ='gallery'),
    url(r'^$photo/<str:ch>',views.viewPhoto, name ='photo'),
    url(r'^$add/',views.addPhoto, name ='add')



]