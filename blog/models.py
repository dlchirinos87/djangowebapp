from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)


    def __str__(self):
        return self.title



