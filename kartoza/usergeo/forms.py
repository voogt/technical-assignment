from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import User_Info


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", max_length=250,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=250,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=250,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    street_address = forms.CharField(label="", max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Street Address'}))
    city = forms.CharField(label="", max_length=250,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    province = forms.CharField(label="", max_length=250,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Province'}))
    country = forms.CharField(label="", max_length=250,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))
    phone = forms.CharField(label="", max_length=250,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'street_address', 'city',
            'province', 'country', 'phone'
        )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ""
        self.fields[
            'username'].help_text = "<span class='form-text text-muted'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>"

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields[
            'password1'].help_text = "<span class='form-text text-muted'><ul class='form-text text-muted'><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password</li><li>Your password can’t be entirely numeric.</li></ul></span>"

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields[
            'password2'].help_text = "<span class='form-text text-muted'>Enter the same password as before, for verification.</span>"


class UserInfoForm(ModelForm):
    street_address = forms.CharField(label="Street Address", max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Street Address'}))
    city = forms.CharField(label="City", max_length=250,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    province = forms.CharField(label="Province", max_length=250,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Province'}))
    country = forms.CharField(label="Country", max_length=250,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))
    phone = forms.CharField(label="Phone", max_length=250,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))

    class Meta:
        model = User_Info
        fields = (
            'street_address', 'city', 'province', 'country', 'phone'
        )


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))
    email = forms.EmailField(label="Email", max_length=250,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="First Name", max_length=250,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="Last Name", max_length=250,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email'
        )


class UpdatePasswordForm(PasswordChangeForm):
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields[
            'new_password1'].help_text = "<span class='form-text text-muted'><ul class='form-text text-muted'><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password</li><li>Your password can’t be entirely numeric.</li></ul></span>"

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields[
            'new_password2'].help_text = "<span class='form-text text-muted'>Enter the same password as before, for verification.</span>"
