from django.conf.urls import url
from .import views


urlpatterns=[

    url(r'^$',views.gallery, name ='gallery'),
    url(r'^photo/(\d+)$',views.viewPhoto, name ='photo'),
    url(r'^add/$',views.addPhoto, name ='add')



]