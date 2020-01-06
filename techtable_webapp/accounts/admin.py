from django.contrib import admin


from .models import Candidate, Employer, InternshipInfo, JobInfo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'jobprofile', 'location', 'mobilenumber', 'website', 'aboutme', 'specialities', 'jobexperience', 'age', 'graduation', 'educationlevel', 'college', 'collegedegree', 'collegepercentage', 'school', 'schoolcertificatetype', 'schoolpercentage', 'jobcompany', 'jobdescription')
    ordering = ('username',)
    search_fields = ('username', 'email')


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email')
    ordering = ('username',)
    search_fields = ('username', 'email')


@admin.register(InternshipInfo)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('jobtitle', 'industryarea', 'monthlysalary_min', 'monthlysalary_max', 'joblocation', 'employment_type', 'number_of_positions', 'experience_required', 'brief_description_of_job', 'job_description')
    search_fields = ('jobtitle', 'joblocation')


@admin.register(JobInfo)
class JobAdmin(admin.ModelAdmin):
    list_display = ('jobprofile', 'numberofopenings', 'jobdescription', 'skillsrequired', 'jobresponsibilities', 'monthlystipend', 'perks', 'jobtype', 'companytype', 'worktime', 'jobbrief', 'joblocation')
    search_fields = ('jobprofile', 'joblocation')