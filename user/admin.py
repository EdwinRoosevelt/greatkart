from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import UserProfile


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'name', 'last_login', 'is_customer', 'is_staff', 'is_superuser']

    ordering = ('-last_login',)
    list_filter = ()
    fieldsets = ()

admin.site.register(UserProfile, CustomUserAdmin)
