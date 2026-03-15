from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Game Data', {'fields': ('points', 'coins', 'is_support')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Game Data', {'fields': ('points', 'coins', 'is_support')}),
    )
    list_display = ('username', 'email', 'points', 'coins', 'is_support', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
