from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import TextInput, EmailInput, Select, FileInput
from .models import UserProfile

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :')
    email = forms.EmailField(max_length=200,label= 'Email :')
    first_name = forms.CharField(max_length=100,label= 'First Name :')
    last_name = forms.CharField(max_length=100,label= 'Last Name :')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User



#this is the Update UserUpdate form
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : TextInput(attrs={'class':'input','placeholder':'username'}),
            'email'     : EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }

COUNTRY = [
    ('IRAN', 'IRAN'),
    ('TURKEY', 'TURKEY'),
    ('USA', 'USA'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city','country','image')
        widgets = {
            'phone'     : TextInput(attrs={'class': 'input','placeholder':'phone'}),
            'address'   : TextInput(attrs={'class': 'input','placeholder':'address'}),
            'city'      : TextInput(attrs={'class': 'input','placeholder':'city'}),
            'country'   : Select(attrs={'class': 'input','placeholder':'country'},choices=COUNTRY),
            'image'     : FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }

