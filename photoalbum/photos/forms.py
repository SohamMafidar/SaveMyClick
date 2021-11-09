from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
    