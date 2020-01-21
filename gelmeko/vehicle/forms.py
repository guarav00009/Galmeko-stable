from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from vendor.models import VendorUser
from vehicle.models import Vehicle,VehicleCategory
from django import forms

class CustomUserCreationForm(forms.ModelForm):
   class Meta:
        model = Vehicle
        fields = ['vehicle_no',]
        widgets = {
            'vehicle_no': forms.TextInput(attrs={'class': 'vTextField form-control'})
            
        }

class VehicleCategoryCreationForm(forms.ModelForm):
   class Meta:
        model = VehicleCategory
        fields = ['category_name',]
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'vTextField form-control'})
            
        }