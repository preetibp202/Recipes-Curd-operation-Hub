from django.db import models
from django.contrib.auth.models import User


class Receipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True) 
    receipe_name = models.CharField(max_length=255, null=True, blank=True)
    receipe_description= models.TextField(null=True, blank=True)
    receipe_image = models.ImageField(upload_to="receipe/")
    
    
    