from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)