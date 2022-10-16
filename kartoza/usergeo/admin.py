from django.contrib import admin
from django import forms
from .models import User_Info, User_Activity


@admin.register(User_Info)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "street_address", "city", "province", "country")
    list_filter = ("city", "province", "country")
    search_fields = ("street_address__startswith", "city__startswith", "province__startswith", "country__startswith")
    # form = InfoForm

    add_exclude = ()
    edit_exclude = ('user_fk',)

    def add_view(self, *args, **kwargs):
        self.exclude = getattr(self, 'add_exclude', ())
        return super(UserInfoAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.exclude = getattr(self, 'edit_exclude', ())
        return super(UserInfoAdmin, self).change_view(*args, **kwargs)


@admin.register(User_Activity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "log_time", "status")
    list_filter = ("log_time",)

    add_exclude = ()
    edit_exclude = ('user_fk',)

    def add_view(self, *args, **kwargs):
        self.exclude = getattr(self, 'add_exclude', ())
        return super(UserActivityAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.exclude = getattr(self, 'edit_exclude', ())
        return super(UserActivityAdmin, self).change_view(*args, **kwargs)
