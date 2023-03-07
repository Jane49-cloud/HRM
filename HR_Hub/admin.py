from django.contrib import admin
from .models import Asset,  Company,  Employee, Notification, Leave
# Register your models here.

admin.site.register(Asset)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(Notification)
