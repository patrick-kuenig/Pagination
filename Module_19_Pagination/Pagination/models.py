from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    published = models.TimeField(auto_now=True)
