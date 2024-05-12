from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields  = ['address', 'user', 'first_name', 'second_name', 'email', 'phone_number', 'image']
        
#         from django import forms
# from .models import CustomUser

# class ProfilePictureForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['profile_picture']
