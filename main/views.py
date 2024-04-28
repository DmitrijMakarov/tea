from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from main.models import *


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
    Product(price=42, type_id=1).save()
    if request.method == "POST":

        review = Reviews(name="Oleg", text="cool", product=Product.objects.get(id=1))
        review.save()
    else:
        review = Reviews(name="Oleg2", text="cool2", product=Product.objects.get(id=1))
        review.save()
        context["reviews"] = Reviews.objects.all()
    return render(request, 'pages/card_product.html', context)


