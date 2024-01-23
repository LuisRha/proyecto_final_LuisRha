from django.contrib import admin

from app.secretaria.cargo.models import Cargo


# Register your models here.
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['cargo']
