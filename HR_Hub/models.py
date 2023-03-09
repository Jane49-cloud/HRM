from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    position = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=False)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    national_id = models.CharField(
        max_length=15, default=None, blank=True, null=True)

    kra_pin = models.CharField(
        max_length=50, default=None, blank=True, null=True)

    REQUIRED_FIELDS = ['username',]
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


# profile model for fields specific to Employer
class Employer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    company = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    # number of employees associated with the employer
    number_of_employees = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.user.email + ' for company ' + self.company


class Employee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Asset(models.Model):
    asset = models.CharField(max_length=50, blank=False, primary_key=True)
    serial_no = models.CharField(max_length=200, blank=False)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=False)


class AssignedAsset(models.Model):
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
