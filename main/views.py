from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from main.forms import LoginUserForm


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
    context = {
        "form": LoginUserForm(),
    }
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            logging_user = authenticate(username=form.username, password=form.password)
            if logging_user is not None:
                login(request, logging_user)
                return redirect('')

            # TODO: Вывод о несуществовании такого пользователя
            return render(request, 'registration/login.html', context)
        else:
            context["form"] = form  # Внутри формы содержатся ошибки
        return render(request, 'registration/login.html', context)

    return render(request, 'registration/login.html', context)


def delivery_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/delivery.html', context)


def card_product(request: WSGIRequest):
    context = {}
    return render(request, 'pages/card_product.html', context)
