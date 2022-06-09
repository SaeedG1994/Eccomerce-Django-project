from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string

from eshop_Order.forms import ShopCartForm, OrderForm
from eshop_Order.models import ShopCart, Order, OrderProduct
from eshop_User.models import UserProfile
from eshop_product.models import Category, Product


def index(request):
    return HttpResponse('order')


@login_required(login_url='/login') #check login user
def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information

    checkproduct=ShopCart.objects.filter(product_id=id) #check product in shopCart
    if checkproduct:
        control= 1 # The product is in the cart
    else:
        control= 0 # The product is not in the cart

    if request.method == 'POST': #if there is post
        form= ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1: #update shop cart
                data = ShopCart.objects.get(product_id=id)
                data.quantity +=form.cleaned_data['quantity']
                data.save()
            else:  #for insert the New product ot add the shopCart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id=id
                data.quantity = form.cleaned_data['quantity']
                data.save()
            messages.success(request,"Product added to shopCart")
            return HttpResponseRedirect(url)

        else: # if there is not post Check for Prevent Product
            if control ==1: #update shop cart
                data = ShopCart.objects.get(product_id=id)
                data.quantity += 1
                data.save()
            else: #insert to shopCart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = 1
                data.save()
            messages.success(request,"Product add to shopCart")
    return HttpResponseRedirect(url)


def shopcart(request):
    category = Category.objects.all()
    current_user= request.user
    shopCart= ShopCart.objects.filter(user_id=current_user.id)
    context={
        'category':category,
        'shopCart':shopCart

    }
    return render(request,'shopCart_Products.html',context)

@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request,"Your Item Delete From ShopCart.")
    return HttpResponseRedirect('/shopcart')


def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        # return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            # ..............

            data = Order()
            data.first_name = form.cleaned_data['first_name']  # get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(10).upper()  # random cod
            data.code = ordercode
            data.save()  #

            # Move shopCart items to Order products item
            shopcart = ShopCart.objects.filter(user_id=current_user.id)
            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id  # Order Id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()
                # ***Reduce quantity of sold product from Amount of Product
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()
                # ***************************************

            ShopCart.objects.filter(user_id=current_user.id).delete()  # Clear & Delete shopcart
            request.session['cart_items'] = 0
            messages.success(request, "Your Order has been completed. Thank you ")
            return render(request, 'Order_completed.html', {'ordercode': ordercode, 'category': category})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'Order_Form.html', context)


