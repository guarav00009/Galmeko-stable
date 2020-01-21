from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from vendor.models import VendorUser
from hospital.models import HospitalUser
from vehicle.models import Vehicle
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import Group
from .models import User
from django.urls import path
from django.conf.urls import include, url
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from .admin_view import vehicle_soft_delete,hospitaluser_soft_delete,category_soft_delete,vendoruser_soft_delete,vehicle_save


class MyAdminSite(admin.AdminSite):
    index_title = ugettext_lazy('Admin')

    def each_context(self, request):
        """
        Return a dictionary of variables to put in the template context for
        *every* page in the admin site.

        For sites running on a subpath, use the SCRIPT_NAME value if site_url
        hasn't been customized.
        """
        self.site_title = ugettext_lazy('User')
        self.index_title = ugettext_lazy('Dashboard')
        self.site_header = ugettext_lazy('GLEMKO')

        script_name = request.META['SCRIPT_NAME']
        site_url = script_name if self.site_url == '/' and script_name else self.site_url
        return {
            'site_title': self.site_title,
            'site_header': self.site_header,
            'site_url': site_url,
            'has_permission': self.has_permission(request),
            'available_apps': self.get_app_list(request),
            'is_popup': False,
        }

    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        my_urls = [
            url('^vehicle/vehicle/delete-vehicle/$',
                self.admin_view(vehicle_soft_delete)),
            url('^hospital/hospitaluser/delete_hospital_user/$',
                self.admin_view(vendoruser_soft_delete)),
            url('^vendor/vendoruser/delete_vendor_user/$',
                self.admin_view(vendoruser_soft_delete)),
            url('^vehicle/vehiclecategory/delete-category/$',
                self.admin_view(category_soft_delete)),
            path('vehicle_save/', self.admin_view(vehicle_save))
                
        ]
        return my_urls + urls


admin_site = MyAdminSite()

class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('full_name', 'email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    list_per_page = 10  # No of records per page
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin_site.register(User, UserAdmin)
