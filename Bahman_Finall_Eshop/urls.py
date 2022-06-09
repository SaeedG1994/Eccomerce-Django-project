"""Bahman_Finall_Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from eshop_Home import views
from eshop_Order import views as OrderViews
from eshop_User import  views as UserViews

urlpatterns = [
    path('',include('eshop_Home.urls')),
    path('order/', include('eshop_Order.urls')),
    path('user/',include('eshop_User.urls'),name='user'),
    path('product/',include('eshop_product.urls')),

    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),


    path('login/',UserViews.login_form,name='login_form'),
    path('logout/',UserViews.logout_func,name='logout_func'),
    path('signup/',UserViews.signup_form,name='signup_form'),

    path('about/',views.about_us,name='about_us'),
    path('contact/',views.contact_us,name='contact_us'),
    path('search/',views.search,name='search'),
    path('faq/',UserViews.faq,name='faq'),

    path('search_auto/',views.search_auto,name='search_auto'),
    path('category/<int:id>/<slug:slug>',views.category_products,name='category_products'),
    path('product/<int:id>/<slug:slug>',views.product_detail,name='product_detail'),
    path('shopcart/',OrderViews.shopcart,name='shopcart'),

]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
