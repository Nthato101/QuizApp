from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class Registration_Form(UserCreationForm):

    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),required=True)
    first_name = forms.CharField(label="First Name",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),required=True)
    last_name = forms.CharField(label="Last Name",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),required=True)
    password1 = forms.CharField(label="Password",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),required=True,
                             help_text=''''<ul class="form-text text-muted small"><li><small>Your password can\'t be too similar to your other personal information.</small>
                             </li><li><small>Your password must contain at least 8 characters.</small>
                             </li><li><small>Your password can\'t be a commonly used password.</small></li><li><small>Your password can\'t be entirely numeric.</small></li></ul>''')
    password2 = forms.CharField(label="Confirm Password",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),required=True,
                             help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>')
    

    class Meta:
        model = User
        fields = ("first_name","last_name", "email", "password1", "password2")


class Login_form(forms.Form):
    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),required=True)
    password = forms.CharField(label="Password",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),required=True)
    