from django.contrib import admin

# Register your models here.
from eshop_home_Slider.models import Home_Slider


class Home_slider_Admin(admin.ModelAdmin):

    list_display = ['title','image','description','link','image_tag']

admin.site.register(Home_Slider,Home_slider_Admin)
