from django.contrib import admin


from .models import CandidateInfo, EmployerInfo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

@admin.register(CandidateInfo)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email')
    ordering = ('username',)
    search_fields = ('username', 'email')


@admin.register(EmployerInfo)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email')
    ordering = ('username',)
    search_fields = ('username', 'email')

