from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

# from techtable_webapp.accounts.models import Candidate, Employer
# Create your models here.


class InternshipInfo(models.Model):
    jobtitle = models.CharField(max_length=100, default='')
    industyarea = models.CharField(max_length=100, default='')
    monthlysalary_min = models.CharField(max_length=15, default='')
    monthlysalary_max = models.CharField(max_length=15, default='')
    joblocation = models.CharField(max_length=100, default='')
    employment_type = models.CharField(max_length=100, default='')
    number_of_positions = models.CharField(max_length=10, default='')
    experience_required = models.CharField(max_length=100, default='')
    brief_description_of_job = models.CharField(max_length=200, default='')
    job_description = models.CharField(max_length=500, default='')


class JobInfo(models.Model):
    jobprofile = models.CharField(max_length=100, default='')
    numberofopenings = models.CharField(max_length=10, default='')
    jobdescription = models.CharField(max_length=500, default='')
    skillsrequired = models.CharField(max_length=100, default='')
    jobresponsibilities = models.CharField(max_length=100, default='')
    monthlystipend = models.CharField(max_length=10, default='')
    perks = models.CharField(max_length=10, default='')
    jobtype = models.CharField(max_length=100, default='')
    companytype = models.CharField(max_length=100, default='')
    worktime = models.CharField(max_length=5, default='')
    jobbrief = models.CharField(max_length=200, default='')
    joblocation = models.CharField(max_length=100, default='')
