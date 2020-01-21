from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from hospital.models import HospitalUser
from django import forms

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'vTextField form-control',
                                      'required': 'true',}))
    class Meta:
        model = HospitalUser
        fields = ['full_name','email','phone','address','status','password']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'vTextField form-control','placeholder': 'Full Name','required': 'true',}),
            'email': forms.TextInput(attrs={'class': 'vTextField form-control','placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'vTextField form-control','placeholder': 'Phone'}),
            'address': forms.TextInput(attrs={'class': 'vTextField form-control','placeholder': 'Address'}),
            'status' : forms.Select(attrs={'class':'vTextField form-control'}),
        }
