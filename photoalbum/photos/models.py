from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null =True,blank = True)
    name = models.CharField(max_length=176,null=False,blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete= models.SET_NULL,null = True,blank = True)
    image = models.ImageField(null =False, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.description
