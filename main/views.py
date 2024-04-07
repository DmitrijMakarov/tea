from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_page(request: WSGIRequest):
   context = {}
   return render(request, 'pages/index.html', context)

def blog_card_page(request: WSGIRequest):
   context = {}
   return render(request, 'pages/blog_card.html', context)

def login_page(request: WSGIRequest):
   context = {}
   return render(request, 'registration/login.html', context)

def delivery_page(request: WSGIRequest):
   context = {}
   return render(request, 'pages/delivery.html', context)

def card_product(request: WSGIRequest):
   context = {}
   return render(request, 'pages/card_product.html', context)
