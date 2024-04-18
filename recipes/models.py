from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class recipe(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    type=models.CharField(max_length=20)
    
