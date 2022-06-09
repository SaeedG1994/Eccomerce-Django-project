from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Avg, Count
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


#THIS CLASS FOR SHOW THE MAIN CATEGORY ON THE ADMIN PANEL
#-----------------------------------------------------------
class Category(MPTTModel):
    STATUS = (
        ('فعال', 'فعال'),
        ('غیر فعال', 'غیر فعال'),
    )
    parent=TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE,verbose_name='سربخش کلی')
    title=models.CharField(max_length=50,verbose_name='عنوان')
    keyword=models.CharField(max_length=255,verbose_name='کلمه کلیدی')
    description=models.TextField(max_length=255,verbose_name='توضیحات')
    image=models.ImageField(blank=True,upload_to='images/',verbose_name='تصویر')
    status=models.CharField(max_length=10,choices=STATUS,verbose_name='وضعیت')
    slug=models.SlugField(null=False,unique=True,verbose_name='آدرس اسلاگ')
    creat_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    update_at=models.DateTimeField(auto_now=True,verbose_name='تاریخ آپدیت')

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی'

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by =['title']


# this Function for spell Category and subCategory from together
#___________________________________________________________________________

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.title]  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])



#THIS CLASS FOR SHOW THE ALL PRODUCTS ON THE ADMIN PANEL
#------------------------------------------------------------------------------

class Product(models.Model):
    STATUS = (
        ('فعال','فعال'),
        ('غیر فعال','غیر فعال'),
    )
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='زیر مجموعه ') #many to one Relation with  Category
    title=models.CharField(max_length=150,verbose_name='عنوان ')
    keyword=models.CharField(max_length=255,verbose_name='کلمه کلیدی ')
    description=models.TextField(max_length=255,verbose_name='توضیح کوتاه ')
    image=models.ImageField(upload_to='images/',null=False,verbose_name='تصویر محصول ')
    price=models.DecimalField(max_digits=12,decimal_places=2,default=0,verbose_name='قیمت محصول ')
    amount=models.IntegerField(default=0,verbose_name='تعداد موجودی محصول ')
    min_amount=models.IntegerField(default=1,verbose_name='حداقل موجودی محصول ')
    slug=models.SlugField(null=False,unique=True,verbose_name='آدرس اسلاگ ')
    details=RichTextUploadingField(verbose_name='جزئیات محصول ')
    status=models.CharField(max_length=10,choices=STATUS,verbose_name='وضعیت محصول ')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت ')
    update_at=models.DateTimeField(auto_now=True,verbose_name='تاریخ آپدیت ')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'image'

#  FOR UNIQ URLS FOR PRODUCTS
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


# FOR RATE ON THE PRODUCT DETAILS
    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg


# FOR Review ON THE PRODUCT DETAILS
    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


#THIS CLASS FOR SHOW IMAGES ONE THE ADMIN PANEL
#_______________________________________________________________
class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=' محصول ')
    title=models.CharField(max_length=50,blank=True,verbose_name='عنوان')
    image=models.ImageField(blank=True,upload_to='images/',verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='تصویر'
        verbose_name_plural='تصاویر محصولات'

#THIS CLASS FOR SHOW IMAGES ONE THE ADMIN PANEL
#_______________________________________________________________

class Comment(models.Model):
    STATUS = (
        ('خوانده شده', 'خوانده شده'),
        ('خوانده نشده', 'خوانده نشده '),
        (' بسته', ' بسته '),
    )

    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    subject=models.CharField(max_length=50,blank=True,verbose_name='موضوع')
    comment=models.CharField(max_length=250,blank=True,verbose_name='نظر کاربر')
    rate=models.IntegerField(default=1,verbose_name='رتبه کاربر')
    ip=models.CharField(max_length=20,blank=True,verbose_name='آی پی کاربر')
    status = models.CharField(max_length=20, choices=STATUS,verbose_name='وضعیت')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    update_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ اپدیت')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name='نظر'
        verbose_name_plural='نظرات'