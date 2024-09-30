from django.contrib import admin
from .models import Role, Department, CustomUser

admin.site.register(CustomUser)
admin.site.register(Role)
admin.site.register(Department)
