from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null= True)
    img = models.ImageField(upload_to= 'images/')
    created = models.DateTimeField(auto_now_add=True)