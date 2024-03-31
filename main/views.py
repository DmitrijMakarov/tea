import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def get_menu_context():
    return [
        {'url_name': 'index', 'name': 'Главная'},
        {'url_name': 'time', 'name': 'Текущее время'},
    ]


def index_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/index.html', context)

def blogs_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/blogs.html', context)



