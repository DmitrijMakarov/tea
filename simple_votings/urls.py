from django.contrib import admin
from django.urls import path

from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_survey_script/', views.create_survey, name='create_survey_script'),
    path('delete_surveys_script/', views.delete_surveys, name='delete_surveys_script'),
    path('', views.index_page, name='index'),
    path('vote/create', views.create_vote_page, name='create_vote'),
    path('vote/answer/<id>', views.vote_answer, name='answer'),
    path('vote/<id>', views.vote_view, name='vote'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.reg_page, name='registration'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.log_out, name='logout'),
    path('error-404', views.page_404, name='error-404')
]
