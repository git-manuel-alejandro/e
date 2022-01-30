from inspect import classify_class_attrs
from tabnanny import verbose
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20 , unique=True)
    description = models.CharField(max_length=255 , blank=True)
    slug = models.CharField(max_length=100 , unique=True)
    cat_image = models.ImageField(upload_to = 'phothos/categories' , blank = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str_(self):
        return self.category_name

