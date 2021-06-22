from django import forms
from django.contrib.auth.models import User
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, EmailValidator
from django.forms.widgets import EmailInput, PasswordInput
from django.contrib.auth.models import User



class SignupForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, 
                                required=True, 
                                validators=[MinLengthValidator(5)], 
                                 
                                )
    email = forms.CharField(label="Email", required=True, widget=EmailInput, validators=[EmailValidator])
    password = forms.CharField(label="Password", max_length=30, widget=PasswordInput,required=True, validators=[])
    re_password = forms.CharField(label="Confirm Password", max_length=30, widget=PasswordInput, required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).first() == None:
            return username
        else:
            raise ValidationError("Username exists")




    def clean_re_password(self):
        confirm_password = self.cleaned_data['re_password']
        original = self.cleaned_data['password']
        if confirm_password != original:
            raise ValidationError("Password Reentered Incorrectly")

        return confirm_password