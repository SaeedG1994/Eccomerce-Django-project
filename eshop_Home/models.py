from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Setting(models.Model):
    STATUS=(
        ('فعال','فعال'),
        ('غیر فعال','غیر فعال')
    )
    title=models.CharField(max_length=150,verbose_name='عنوان ')
    keywords=models.CharField(max_length=250,verbose_name='کلمه کلیدی ')
    description=models.CharField(max_length=250,verbose_name='توضیحات ')
    company_name=models.CharField(max_length=50,verbose_name='نام شرکت ')
    address=models.CharField(blank=True,max_length=100,verbose_name='آدرس ')
    phone=models.IntegerField(verbose_name='تلفن ثابت ')
    mobile=models.IntegerField(verbose_name='موبایل ')
    email=models.CharField(max_length=150,verbose_name='ایمیل ')
    smpt_server=models.CharField(blank=True,max_length=50,verbose_name='smtp سرور ')
    smtp_email=models.CharField(blank=True,max_length=50,verbose_name='smtp ایمیل')
    smtp_password=models.CharField(blank=True,max_length=10,verbose_name='smtp پسورد')
    smtp_port=models.CharField(blank=True,max_length=5,verbose_name='smtp پورت')
    icon=models.ImageField(blank=True,upload_to='images/',verbose_name='آیکون/لوگو')
    instagram=models.CharField(max_length=50,verbose_name='نام حساب در ایسنتاگرام ')
    youtube=models.CharField(max_length=50,verbose_name='نام کانال در یوتیوب ')
    twitter=models.CharField(max_length=50,verbose_name='نام صفحه در توییتر ')
    about_us=RichTextUploadingField(verbose_name='درباره ی ما')
    contact_us=RichTextUploadingField(verbose_name='تماس با ما ')
    references=RichTextUploadingField(verbose_name='منابع ')
    status=models.CharField(max_length=10,choices=STATUS,verbose_name='وضعیت ')
    creat_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    update_at=models.DateTimeField(auto_now=True,verbose_name='آپدیت خودکار')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural='تنظیمات کلی'

# THIS CLASS FOR CONTACT MESSAGE IN THE WEB PAGE : CONTACT US
#____________________________________________________
class ContactMessage(models.Model):
    STATUS=(
        ('جدید','جدید'),
        ('خوانده شده','خوانده شده'),
        ('بسته','بسته'),
    )
    name=models.CharField(max_length=20,verbose_name='نام')
    email=models.CharField(max_length=60,verbose_name='ایمیل')
    subject=models.CharField(blank=True,max_length=50,verbose_name='موضوع')
    message=models.TextField(blank=True,max_length=255,verbose_name='پیام شما')
    status=models.CharField(max_length=10,choices=STATUS,default='جدید',verbose_name='وضعیت پیام')
    ip=models.CharField(blank=True,max_length=20,verbose_name='آی پی کاربر')
    note=models.CharField(blank=True,max_length=100,verbose_name='یادداشت')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    update_at=models.DateTimeField(auto_now=True,verbose_name='تاریخ اپدیت')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='پیام'
        verbose_name_plural='بخش تماس با ما'

# THIS CLASS FOR ّFAQ  IN THE WEB PAGE
#____________________________________________________

class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    ordernumber = models.IntegerField(verbose_name='شماره سفارش ')
    question =RichTextUploadingField(max_length=200,verbose_name='سوالات متداول')
    answer = RichTextUploadingField(verbose_name='جواب سوال ')
    status = models.CharField(max_length=10, choices=STATUS,verbose_name='وضعیت سوال ')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد ')
    update_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ آپدیت ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name='سوال'
        verbose_name_plural='بخش سوالات متداول'