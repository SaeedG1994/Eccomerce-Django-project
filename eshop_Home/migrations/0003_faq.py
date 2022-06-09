# Generated by Django 3.2.9 on 2021-11-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_Home', '0002_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField(verbose_name='شماره سفارش ')),
                ('question', models.CharField(max_length=200, verbose_name='سوالات متداول')),
                ('answer', models.TextField(verbose_name='جواب سوال ')),
                ('status', models.CharField(choices=[('فعال', 'فعال'), ('غیر فعال', 'غیر فعال')], max_length=10, verbose_name='وضعیت سوال ')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت ')),
            ],
            options={
                'verbose_name': 'سوال',
                'verbose_name_plural': 'بخش سوالات متداول',
            },
        ),
    ]
