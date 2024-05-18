from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_page(request: WSGIRequest):
   context = {}
   return render(request, 'pages/index.html', context)

def blog1(request: WSGIRequest):
   context = {}
   return render(request, 'pages/blog1.html', context)

def blog2(request: WSGIRequest):
   context = {}
   return render(request, 'pages/blog2.html', context)

def blog3(request: WSGIRequest):
   context = {}
   return render(request, 'pages/blog3.html', context)

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
   return render(request, 'pages/card_product.html', context)
