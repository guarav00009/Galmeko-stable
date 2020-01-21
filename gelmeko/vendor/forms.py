from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from vendor.models import VendorUser
from django import forms

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    # class Meta:
    #     model = VendorUser
    #     fields = '__all__'

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     VendorUser.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         VendorUser.save()
    #     return user


class CustomUserChangeForm(forms.ModelForm):
    pass
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    # class Meta:
    #     model = VendorUser
    #     fields = ('email',)

