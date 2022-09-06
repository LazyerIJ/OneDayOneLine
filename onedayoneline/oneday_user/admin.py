from django.contrib import admin
from .models import Oneday_user

# Register your models here.


class Oneday_user_Admin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Oneday_user, Oneday_user_Admin)