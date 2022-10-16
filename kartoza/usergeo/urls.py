from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('profile/', views.view_profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('edit_basic/', views.edit_basic, name="edit_basic"),
    path('edit_info/', views.edit_info, name="edit_info"),
    path('change_password/', views.change_password, name="change_password"),
    path('get/ajax/get_users', views.get_users, name="get_users")
]