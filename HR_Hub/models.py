from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    number_of_employees = models.IntegerField()
    employer = models.OneToOneField(User, on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    kra_pin = models.CharField(max_length=20, null=True, blank=True)


class Asset(models.Model):
    name = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(
        Employee, null=True, blank=True, on_delete=models.CASCADE)


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    approved = models.BooleanField(default=False)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
