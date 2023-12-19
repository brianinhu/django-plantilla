from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=64, default='Title')
    content = models.TextField(null=True)
    image = models.ImageField(null=True)
    published_time = models.BooleanField(default=False)

    pub_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=64, default='Category')
    description = models.TextField(null=True)

    created = models.DateField(null=True)

