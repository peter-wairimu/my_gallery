from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    path('',views.gallery, name ='gallery'),
    path('photo/<str:pk>/',views.viewPhoto, name ='photo'),
    path('add/',views.addPhoto, name ='add'),
    path('search_results/',views.search_results, name='search_results'),
    path('delete_event/<str:pk>',views.delete_event,name='delete-event'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)