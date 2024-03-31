from django.contrib import admin
from django.urls import path

from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index_page, name='index'),
    path('blogs/', views.blogs_page, name='blogs'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
