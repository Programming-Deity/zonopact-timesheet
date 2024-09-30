from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='role_list'),
    path('roles/add/', views.add_role, name='add_role'),
    path('login', views.loginUser, name='login'),
    path('register', views.registerUser, name='register'),

]
