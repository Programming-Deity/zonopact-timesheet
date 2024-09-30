from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.password_validation import validate_password
from.models import CustomUser, Role


alphanumeric_text = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=50, validators=[alphanumeric_text], required=True)
    email = forms.EmailField(label='Email', max_length=100, validators=[EmailValidator()], required=True)
   
    
    class Meta:
        model = CustomUser
        fields = ('username','employee_id', 'email', 'department', 'role', 'is_manager')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 character long")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Password do not match.')
        return password2



class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'department', 'platform_access']
    








