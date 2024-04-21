from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import models
from django.http import JsonResponse
from django.template.loader import render_to_string



def index_page(request: WSGIRequest):
   context = {}
   return render(request, 'pages/index.html', context)

def blogs_page(request: WSGIRequest):
   context = {}
   return render(request, 'pages/blogs.html', context)

def delivery_page(request: WSGIRequest):
   context = {}
   return render(request, 'pages/delivery.html', context)

def card_product(request: WSGIRequest):
   context = {}
   return render(request, 'pages/card_product.html', context)


def profile_page(request: WSGIRequest):
    user = User_c.objects.get(username=request.user.username)
    email = user.email

    context = {
        'user': request.user,
        'email': email

    }
    return render(request, 'pages/profile.html', context)


def reg_page(request: WSGIRequest):
    if request.method == "POST":
        if 'username' in request.POST:
            # Получение данных
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if User_c.objects.filter(username=username).exists():
                messages.error(request, "Имя пользователя уже занято")
                return render(request, 'pages/reg.html')
            elif User_c.objects.filter(email=email).exists():
                messages.error(request, "На данную почту уже зарегестрирован аккаунт. Попробуйте войти в аккаунт")
                return render(request, 'pages/reg.html')
            else:
                # Создание объекта
                logging_user = User_c.objects.create_user(username, email, password)
                # Запись объекта в БД
                logging_user.save()
                messages.success(request, "Вы успешно создали аккаунт")

                return redirect('login')

    return render(request, 'pages/reg.html')


def login_page(request: WSGIRequest):
    if request.method == "POST":
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']
        logging_user = authenticate(username=login_username, password=login_password)

        if logging_user is not None:
            login(request, logging_user)
            messages.success(request, "Вы успешно вошли в аккаунт аккаунт")
            return redirect('profile')
        messages.error(request, "Неправильно введено имя пользователя или пароль")
        return redirect('login')

    return render(request, 'registration/login.html')


def log_out(request):
    logout(request, )
    return redirect('/')

