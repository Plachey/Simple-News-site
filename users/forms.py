from django.contrib.auth import forms
from .models import CustomUser


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age',)


class CustomUserChangeForm(forms.UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age',)
