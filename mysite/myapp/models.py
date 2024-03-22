from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=64, default='Title')
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='articles', null=True)
    published_time = models.BooleanField(default=False)

    pub_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        if self.published_time:
            publicado = "Publicado"
        else:
            publicado = "No Publicado / En Revisión"
        return f"{self.title}. Creado el: {self.pub_time}. {publicado}"


class Category(models.Model):
    name = models.CharField(max_length=64, default='Category')
    description = models.TextField(null=True)
    created = models.DateField(null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}. Creado el: {self.created}"
