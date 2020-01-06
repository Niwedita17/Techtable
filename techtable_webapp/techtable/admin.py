from django.contrib import admin

# Register your models here.
from .models import InternshipInfo, JobInfo

#admin.site.register(CandidateInfo)
#admin.site.register(EmployerInfo)
admin.site.register(InternshipInfo)
admin.site.register(JobInfo)
