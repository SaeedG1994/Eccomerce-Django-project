# Generated by Django 3.2.9 on 2021-11-29 07:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_Home', '0003_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='جواب سوال '),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=200, verbose_name='سوالات متداول'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10, verbose_name='وضعیت سوال '),
        ),
    ]