from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from main.models import *
from .models import Product

from main.forms import LoginUserForm, RegisterUserForm, ReviewForm


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

def card_product(request: WSGIRequest):
    context = {}
    data = Type.objects.all()
    if len(data) == 0:
        Type(name="Tea", products={}).save()
    data = Product.objects.all()
    if len(data) == 0:
        Product(type=Type.objects.get(id=1), price=42).save()

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

def delivery_page(request: WSGIRequest):
   context = {}
   return render(request, 'pages/delivery.html', context)


def catalog(request: WSGIRequest):
    products = Product.objects.all()
    for i in range(len(products)):
        products[i].upprice = products[i].price * 1.2  - 0.01
        products[i].price = products[i].price - 0.01
    context = {"products": products}
    return render(request, 'pages/Products_catalog.html', context)

def product(request: WSGIRequest):
    context = {}
    return render(request, 'pages/product.html', context)

def help(request: WSGIRequest):
    context = {}
    return render(request, 'pages/help_page.html', context)
