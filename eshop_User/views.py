from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from eshop_Home.models import FAQ
from eshop_Order.models import Order, OrderProduct
from eshop_User.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from eshop_User.models import UserProfile
from eshop_product.models import Category, Comment


def index(request):
    catgory= Category.objects.all()
    current_user= request.user
    profile= UserProfile.objects.get(user_id=current_user.id)
    context={
        'category':catgory,
        'profile':profile
    }
    return render(request,'user_profile.html',context)


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            current_user=request.user
            userProfile=UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] =userProfile.image.url
            #Redirect to success page
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'login_form.html',context)

# THIS FUNCTION FOR LOG OUT USERS
#__________________________________________________

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')




# THIS FUNCTION FOR SIGNUP  USERS ON THE SITE
#__________________________________________________

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')


    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'signup_form.html', context)


@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login') # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form,'category': category
                       })


@login_required(login_url='/login') # check login
def user_orders(request):
    category=Category.objects.all()
    current_user= request.user
    orders=Order.objects.filter(user_id=current_user.id)
    context={
        'category':category,
        'orders':orders
    }
    return render(request,'user_orders.html',context)


@login_required(login_url='/login') # Check login
def user_orderdetail(request,id):
    category= Category.objects.all()
    current_user= request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderItems=OrderProduct.objects.filter(order_id=id)
    context={
        'category':category,
        'order':order,
        'orderItems':orderItems
    }
    return render(request,'user_order_detail.html',context)

@login_required(login_url='/login')
def user_orders_product(request):
    category = Category.objects.all()
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'order_product': order_product,

    }
    return render(request, 'user_order_Products.html', context)


@login_required(login_url='/login') # Check login
def user_order_product_detail(request,id,oid):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderItems = OrderProduct.objects.filter(id=id,user_id=current_user.id)
    context = {
        'category': category,
        'order': order,
        'orderItems': orderItems
    }
    return render(request, 'user_order_detail.html', context)


def user_comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'comments': comments,
    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login') # Check login
def user_deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user).delete()
    messages.success(request,'Comment deleted.')
    return HttpResponseRedirect('/user/comments')


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.filter(status=True).order_by("ordernumber")
    context = {
        'category': category,
        'faq': faq,
    }
    return render(request, 'faq.html', context)
