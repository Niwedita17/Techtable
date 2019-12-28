from django.contrib import admin

# Register your models here.
from .models import CandidateInfo, EmployerInfo

admin.site.register(CandidateInfo)
admin.site.register(EmployerInfo)
