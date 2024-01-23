from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase

from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdminBase):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {
         'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Información adcional', {'fields': ('nickname',)}),
    )
