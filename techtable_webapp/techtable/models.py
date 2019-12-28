from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


# Create your models here.

class CandidateInfo(models.Model):
    username = models.CharField(primary_key=True, max_length=8, validators=[
        RegexValidator(
            regex='^C[0-9]{2}[A-Z]{2}[0-9]{3}$',
            message='Username should be of form e.g C20CO101',
            code='invalid_candidate_Username'),
                                ])
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)



class EmployerInfo(models.Model):
    username = models.CharField(primary_key=True, max_length=8, validators=[
        RegexValidator(
            regex='^E[0-9]{2}[A-Z]{2}[0-9]{3}$',
            message='Username should be of form e.g E19CO101',
            code='invalid_employer_Username'),
                                ])
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

