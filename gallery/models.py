from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)


    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    img = models.ImageField(null=False,blank =False)
    description = models.CharField(max_length=600,null=False,blank=False)


    def __str__(self):
        return self.description

    @classmethod
    def search_by_title(cls,search_term):
        gallery = cls.objects.filter(title__icontains=search_term)
        return gallery