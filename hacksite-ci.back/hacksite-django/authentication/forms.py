from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ("username", "password")


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
