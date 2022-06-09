from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from eshop_Home.models import Setting
from eshop_product.forms import CommentForm
from eshop_product.models import Comment, Category

def index(request):
    return HttpResponse ('product page')


def addcomment(request,id):
    url = request.META.get('HTTP_REFERER') # get the last url
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()  # create relation with model
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id=id
            current_user=request.user
            data.user_id=current_user.id
            data.save()  # save data to table
            messages.success(request, "Your review has ben sent. Thank you for your interest.")
            return HttpResponseRedirect(url)


    return HttpResponseRedirect(url)

