import json
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from eshop_home_Slider.models import Home_Slider
from .forms import ContactForm,SearchForm
# Create your views here.
from eshop_Home.models import Setting, ContactMessage
from eshop_product.models import Category, Product, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    homeSlider=Home_Slider.objects.all()
    products_latest = Product.objects.all().order_by('-id')[:4]  # Last  4 products
    products_picked = Product.objects.all().order_by('?')[:4]  # Random 4 products

    page = 'home'
    context = {
        'setting': setting,
        'category': category,
        'homeSlider':homeSlider,
        'products_latest':products_latest,
        'products_picked':products_picked,

    }
    return render(request, 'shared/index.html', context)


def about_us(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
    }
    return render(request, 'about_us.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create a relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save information  on the table
            messages.success(request, "your message has be sent. Thank you for your Message!")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm
    context = {
        'setting': setting, 'form': form,'category':category
    }
    return render(request, 'contact.html', context)


def category_products(request,id,slug):
    category=Category.objects.all()
    products=Product.objects.filter(category_id=id)
    context={
        'category':category,
        'products':products
    }
    return render(request,'category_products.html',context)


def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title +" > " + rs.category.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request,id,slug):
    category = Category.objects.all()
    product=Product.objects.get(pk=id)
    images= Images.objects.filter(product_id=id)
    comments= Comment.objects.filter(product_id=id,status='خوانده شده')
    context = {
        'category':category,
        'product':product,
        'images':images,
        'comments':comments
    }

    return render(request, 'product_detail.html', context)


