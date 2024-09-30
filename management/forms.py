# from crispy_forms.templatetags.crispy_forms_field import css_class
from django import forms
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from.models import CustomUser, Role


alphanumeric_text = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'department', 'role', 'is_manager')



class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'department', 'platform_access']
    








