from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    signup_confirmation = models.BooleanField(default=False)
    jobprofile = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=200, default='')
    mobilenumber = models.CharField(max_length=10, default='', validators=[RegexValidator(regex='^[0-9]{10}$'), ])
    website = models.CharField(max_length=50, default='')
    aboutme = models.CharField(max_length=200, default='')
    specialities = models.CharField(max_length=100, default='')
    jobexperience = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=3, default='')
    graduation = models.CharField(max_length=100, default='')
    educationlevel = models.CharField(max_length=50, default='')
    college = models.CharField(max_length=100, default='')
    collegedegree = models.CharField(max_length=50, default='')
    collegepercentage = models.CharField(max_length=2, default='')
    school = models.CharField(max_length=100, default='')
    schoolcertificatetype = models.CharField(max_length=100, default='')
    schoolpercentage = models.CharField(max_length=2, default='')
    jobcompany = models.CharField(max_length=100, default='')
    # jobstartdate = models.DateField()
    # jobenddate = models.DateField()
    jobdescription = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_candidate_signal(sender, instance, created, **kwargs):
    if created:
        Candidate.objects.create(user=instance)
    instance.candidate.save()


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_employer_signal(sender, instance, created, **kwargs):
    if created:
        Employer.objects.create(user=instance)
    instance.employer.save()


class InternshipInfo(models.Model):
    jobtitle = models.CharField(max_length=100, default='')
    industryarea = models.CharField(max_length=100, default='')
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
