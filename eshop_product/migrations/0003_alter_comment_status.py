# Generated by Django 3.2.9 on 2021-11-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('خوانده شده', 'خوانده شده'), ('خوانده نشده', 'خوانده نشده '), (' بسته', ' بسته ')], max_length=20, verbose_name='وضعیت'),
        ),
    ]
