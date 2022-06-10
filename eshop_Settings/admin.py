from django.contrib import admin

# Register your models here.
from eshop_User.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','address','city','country','image_tag']


admin.site.register(UserProfile,UserProfileAdmin)