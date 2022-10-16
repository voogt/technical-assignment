import functools

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm, UserInfoForm, EditProfileForm, UpdatePasswordForm
from django.contrib.auth.models import User
from .models import User_Info
import requests
import urllib.parse
from geopy.geocoders import Nominatim


def get_location(street_addr, city, province, country):
    full_addr = f"{street_addr}, {city}, {country}"
    geolocator = Nominatim(user_agent="myGeocoder")
    try:
        location = geolocator.geocode(full_addr)
        location_dict = {
            "lat": location.latitude,
            "lon": location.longitude
        }
        return location_dict
    except AttributeError:
        return 0


def login_required(function):
    def wrap(request, *args, **kwargs):
        session = request.session # this is a dictionary with session keys
        user = request.user
        if user.is_authenticated:
            # the decorator is passed and you can handle the request from the view
            return function(request, *args, **kwargs)
        else:
            return redirect('usergeo:login')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def index(request):
    return render(request, "usergeo/index.html")


def get_users(request):
    if request.method == "GET":
        user_list = []
        users_obj = User.objects.filter(is_superuser=0)
        for user in users_obj:
            info_obj = User_Info.objects.get(user_fk=user.id)

            location = get_location(
                street_addr=info_obj.street_address,
                city=info_obj.city,
                province=info_obj.province,
                country=info_obj.country,
            )

            if location != 0:
                new_dict = {
                    "user_id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "email": user.email,
                    "phone": info_obj.phone,
                    "street_address": info_obj.street_address,
                    "city": info_obj.city,
                    "province": info_obj.province,
                    "country": info_obj.country,
                    "lat": location["lat"],
                    "lon": location["lon"]
                }
                user_list.append(new_dict)
            context = {'users': user_list}
        return JsonResponse(context, status=200)
    return JsonResponse({}, status=200)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have logged in"))
            return redirect('usergeo:index')
        else:
            messages.success(request, ("Incorrect username/password"))
            return redirect('usergeo:login')
    else:
        return render(request, "usergeo/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out ..."))
    return redirect('usergeo:index')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            street_address = form.cleaned_data["street_address"]
            city = form.cleaned_data["city"]
            province = form.cleaned_data["province"]
            country = form.cleaned_data["country"]
            phone = form.cleaned_data["phone"]

            isLocation = get_location(street_addr=street_address, city=city, province=province, country=country)

            if isLocation != 0:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                                last_name=last_name)
                user.save()
                user_info = User_Info(user_fk=user, street_address=street_address, city=city, province=province,
                                      country=country, phone=phone)
                user_info.save()

                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "Edit was successful!")
                return redirect('usergeo:index')
            else:
                messages.success(request, "Your address could not be converted to latitude and longitude!")
                context = {'form': form}
                return render(request, "usergeo/register.html", context)
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, "usergeo/register.html", context)


@login_required
def edit_profile(request):
    user_info_obj = User_Info.objects.get(user_fk=request.user.id)
    form_basic = EditProfileForm(instance=request.user)
    form_info = UserInfoForm(instance=user_info_obj)
    context = {"form_basic": form_basic, "form_info": form_info}
    return render(request, 'usergeo/edit_profile.html', context)


def edit_basic(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated!")
            return redirect('usergeo:edit_profile')
    else:
        messages.success(request, "Profile Updated!")
        return redirect('usergeo:edit_profile')
    return redirect('usergeo:edit_profile')


def edit_info(request):
    if request.method == "POST":
        user_info_obj = User_Info.objects.get(user_fk=request.user.id)
        form = UserInfoForm(request.POST, instance=user_info_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated!")
            return redirect('usergeo:edit_profile')
    else:
        return redirect('usergeo:edit_profile')
    return redirect('usergeo:edit_profile')


@login_required
def change_password(request):
    if request.method == "POST":
        form = UpdatePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Updated!")
            return redirect('usergeo:index')
    else:
        form = UpdatePasswordForm(user=request.user)

    context = {"form": form}
    return render(request, 'usergeo/change_password.html', context)


