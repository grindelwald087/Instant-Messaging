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
            'class': 'form-control border border-dark-subtle',
            'placeholder': 'Enter email'
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if users.objects.filter(username=username).exists():
            self.add_error('username', 'Username already exist, choose another.')
        return username 
    
# Composing Message Form
class compose_msg_form(forms.Form):
    compose_msg = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control custom_message',
            'id': 'custom_message',
            'maxlength': 200,
        })
    )