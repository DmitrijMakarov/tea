from django.contrib import admin
from django.urls import path

from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index_page, name='index'),
   path('blogs/', views.blogs_page, name='blogs'),
   path('login/', views.login_page, name='login'),
   path('delivery/', views.delivery_page, name='delivery'),
   path('card_product/', views.card_product, name='card_product'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

