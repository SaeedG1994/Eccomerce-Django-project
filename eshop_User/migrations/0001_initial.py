# Generated by Django 3.2.9 on 2021-11-24 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='همراه ')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='آدرس ')),
                ('city', models.CharField(blank=True, max_length=20, verbose_name='شهر ')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='کشور ')),
                ('image', models.ImageField(blank=True, upload_to='images/users/', verbose_name='تصویر ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر ')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]