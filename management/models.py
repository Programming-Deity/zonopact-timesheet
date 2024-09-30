from django.contrib.auth.models import AbstractUser
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)


    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    platform_access = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    