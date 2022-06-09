from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from eshop_product.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name='کاربر ')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,verbose_name='محصول ')
    quantity = models.IntegerField(verbose_name='تعداد ')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name='سبد'
        verbose_name_plural='  بخش سبد خرید'

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)



# THIS IS THE ORDER CLASS
#_____________________________________________________

class Order(models.Model):
    STATUS = (
        ('جدید', 'جدید'),
        ('انجام شده', 'انجام شده'),
        ('در حال آماده سازی', 'در حال آماده سازی'),
        ('در حال ارسال', 'در حال ارسال'),
        ('تحویل مرسوله به مشتری', 'تحویل مرسوله به مشتری'),
        ('کنسل شده', 'کنسل شده'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name='کاربر ')
    code = models.CharField(max_length=10, editable=False,verbose_name='کد رهگیری محصول ' )
    first_name = models.CharField(max_length=10,verbose_name='نام ')
    last_name = models.CharField(max_length=10,verbose_name=' نام خانوادگی')
    phone = models.CharField(blank=True, max_length=20,verbose_name='همراه ')
    address = models.CharField(blank=True, max_length=150,verbose_name='آدرس ')
    city = models.CharField(blank=True, max_length=20,verbose_name=' شهر ')
    country = models.CharField(blank=True, max_length=20,verbose_name=' کشور ')
    total = models.FloatField(verbose_name='مجموعه خرید')
    status=models.CharField(max_length=25,choices=STATUS,default='New',verbose_name='وضعیت محصول ')
    ip = models.CharField(blank=True, max_length=20,verbose_name='شناسه آی پی ')
    adminnote = models.CharField(blank=True, max_length=100,verbose_name='یاداشت مدیر ')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد ')
    update_at=models.DateTimeField(auto_now=True,verbose_name='تاریخ اپدیت ')


    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'بخش سفارش'


# THIS IS THE ORDER PRODUCT
#_____________________________________________________

class OrderProduct(models.Model):
    STATUS = (
        ('جدید', 'جدید'),
        ('انجام شده', 'انجام شده'),
        ('کنسل شده', 'کنسل شده'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='سفارش مربوط ')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='کاربر سفارش دهنده ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول سفارش داده شده ')

    quantity = models.IntegerField(verbose_name='تعداد ')
    price = models.FloatField(verbose_name='قیمت ')
    amount = models.FloatField(verbose_name='مقدار محصول')
    status = models.CharField(max_length=20, choices=STATUS, default='New',verbose_name='وضعیت سفارش محصول ')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد ')
    update_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ اپدیت ')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'سفارش محصول'
        verbose_name_plural = 'بخش سفارش محصول'