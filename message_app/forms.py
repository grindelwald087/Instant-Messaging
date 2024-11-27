import re

from django import forms
from .models import users

# Login form
class login_form(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'id': 'uname',
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Enter username'
        })
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Enter password'
        })
    ) 
    
# Register form
class register_form(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="Gender",
        initial='Male'
    )

    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'id': 'fname',
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Enter first name'
        })
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'id': 'lname',
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Enter last name'
        })
    )
    email = forms.CharField(
        max_length=50,
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'class': 'form-control border rounded border-dark-subtle',
            'placeholder': 'Enter email'
        })
    )
    otp = forms.CharField(
        max_length=8,
        widget=forms.TextInput(attrs={
            'id': 'otp',
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Enter OTP'
        })
    )
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'id': 'uname',
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Enter username'
        })
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Enter password'
        })
    )
    confirm_password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'id': 'confirm_password',
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Retype password'
        })
    )

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if re.search(r'\d', first_name):
            self.add_error('first_name', 'Invalid first name.')
            
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if re.search(r'\d', last_name):
            self.add_error('last_name', 'Invalid last name.')

        return last_name
        

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if users.objects.filter(username=username).exists():
            self.add_error('username', 'Username already exist, choose another.')

        if len(username) < 3:
            self.add_error('username', 'Username must be at least 3 characters long.')

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
        
        domain = email.split('@')[-1]
        
        if domain not in allowed_domains:
            self.add_error('email', 'Invalid email address.')

        return email
    
    def clean(self):
        cleaned_data = super().clean()
        
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and len(password) < 8:
            self.add_error('password', 'Password must be at least 8 characters long.')
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')

        return cleaned_data
    
# Composing Message Form
class compose_msg_form(forms.Form):
    compose_msg = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control custom_message',
            'id': 'custom_message',
            'maxlength': 1000,
        })
    )