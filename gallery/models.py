from django.db import models

# Create your models here.
class Images(models.Model): 
    category = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='images')