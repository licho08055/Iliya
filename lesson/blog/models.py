from audioop import reverse
from django.db import models
from django.urls import reverse
from audioop import reverse as audio_reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=1,max_digits=1000)
    
    
    def get_absolute_url(self):
        return reverse('blog:blog',kwargs={'id': self.id})