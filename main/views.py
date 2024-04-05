from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/index.html', context)

def blogs_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/blogs.html', context)

def login_page(request: WSGIRequest):
    context = {}
    return render(request, 'registration/login.html', context)

def delivery_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/delivery.html', context)
