from django.contrib import admin
from django.urls import path

from main import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('blog/', views.blog_card_page, name='blog'),
    path('index/', views.index_page, name='index'),
    path('blogs/', views.blogs_page, name='blogs'),
    path('login/', views.login_page, name='login'),
    path('delivery/', views.delivery_page, name='delivery'),
    path('card_product/', views.card_product, name='card_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_page, name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/', views.product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

