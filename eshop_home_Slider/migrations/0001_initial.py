# Generated by Django 3.2.9 on 2021-11-18 10:37

from django.db import migrations, models
import eshop_home_Slider.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان عکس')),
                ('link', models.URLField(max_length=100, verbose_name='لینک تصویر')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_home_Slider.models.upload_image_path, verbose_name='تصویر اسلایدر')),
            ],
            options={
                'verbose_name': 'تصویر اسلایدر',
                'verbose_name_plural': 'اسلایدر اصلی',
            },
        ),
    ]