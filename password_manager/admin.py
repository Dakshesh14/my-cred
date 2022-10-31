from django.contrib import admin

from .models import PasswordStore


@admin.register(PasswordStore)
class PasswordStoreAdmin(admin.ModelAdmin):
    pass
