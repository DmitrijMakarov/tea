from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Product

from main.forms import LoginUserForm, RegisterUserForm


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
            logging_user = authenticate(username=form.data["username"], password=form.data["password"])
            if logging_user is not None:
                login(request, logging_user)
                return redirect('/')

            # TODO: Вывод о несуществовании такого пользователя
            return render(request, 'registration/login.html', context)
        else:
            context["form"] = form  # Внутри формы содержатся ошибки

    return render(request, 'registration/login.html', context)


def register_page(request: WSGIRequest):
    context = {
        "form": RegisterUserForm(),
    }
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if form.data["password1"] == form.data["password2"]:
                user = User.objects.create_user(form.data["username"], form.data["email"], form.data["password1"])
                return redirect("/login")
            else:
                pass
                # Вывод об ошибке ввода пароля
        else:
            context["form"] = form  # Внутри формы содержатся ошибки

    return render(request, "registration/reg.html", context)


def delivery_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/delivery.html', context)


def card_product(request: WSGIRequest):
    context = {}
    return render(request, 'pages/card_product.html', context)

def catalog(request: WSGIRequest):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/Products_catalog.html', context)

def product(request: WSGIRequest):
    context = {}
    return render(request, 'pages/product.html', context)
