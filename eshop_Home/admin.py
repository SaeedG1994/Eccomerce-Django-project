from django.contrib import admin

# Register your models here.
from eshop_Home.models import Setting, ContactMessage, FAQ


# THIS CLASS FOR SHOW THE SITE SETTING ON THE ADMIN PANEL
#____________________________________________________
class AdminSetting(admin.ModelAdmin):

    list_display = ['title','company_name','creat_at','update_at']




# THIS CLASS FOR SHOW THE CONTACT US ON THE  ADMIN PANEL
#____________________________________________________
class AdminContactUS(admin.ModelAdmin):
    list_display=['name','subject','message','ip','status','create_at']
    readonly_fields = ['name','email','subject','message','ip','create_at',]
    list_filter = ['status']



# THIS CLASS FOR   FAQ   THE  ADMIN PANEL
#____________________________________________________
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'ordernumber', 'status']
    list_filter = ['status']



admin.site.register(FAQ, FAQAdmin)
admin.site.register(ContactMessage,AdminContactUS)
admin.site.register(Setting,AdminSetting)