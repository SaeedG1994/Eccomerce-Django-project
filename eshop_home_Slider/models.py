import os

from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


def get_filename_ext(filepath):
    base_name= os.path.basename(filepath)
    name,ext= os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance,filename):
    name,ext= get_filename_ext(filename)
    final_name=f"{instance.id} - {instance.title}- {ext}"
    return f"Sliders/{final_name}"

class Home_Slider(models.Model):
    title= models.CharField(max_length=150,verbose_name='عنوان عکس')
    link= models.URLField(max_length=100,verbose_name='لینک تصویر')
    description= models.TextField(blank=True,verbose_name='توضیحات')
    image= models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name='تصویر اسلایدر')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))


    image_tag.short_description = 'image'

    class Meta:
        verbose_name='تصویر'
        verbose_name_plural='تصاویر اسلایدر'
