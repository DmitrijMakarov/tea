from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from main.models import *

from main.forms import ReviewForm

def index_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/index.html', context)


def blog_card_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/blog_card.html', context)


def blogs_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/blogs.html', context)


def login_page(request: WSGIRequest):
    context = {}
    return render(request, 'registration/login.html', context)


def delivery_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/delivery.html', context)


def card_product(request: WSGIRequest):
    context = {}
    #Type(name="Tea", products={}).save()
    #Product(type=Type.objects.get(id=1), price=42).save()
    current_form = ReviewForm(request.POST)
    if current_form.is_valid():
        value = current_form.cleaned_data['str']
        review = Reviews(name="Oleg", text=value, product=Product.objects.get(id=1))
        review.save()
    context["form"] = current_form
    #review = Reviews(name="Oleg2", text="cool2", product=Product.objects.get(id=1))
    #review.save()
    context['form'] = ReviewForm()
    context["reviews"] = Reviews.objects.all()
    return render(request, 'pages/card_product.html', context)


