from django.urls import path, include
from . import views


app_name = 'auth_admin'
urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.My_login, name='login'),
    path('logout/', views.My_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('register_success/', views.register_success, name='register_success'),

]







