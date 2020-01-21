from django.contrib import admin
from .forms import CustomUserCreationForm,VehicleCategoryCreationForm
from django.utils.html import format_html
from vehicle.models import Vehicle
from vehicle.models import VehicleCategory
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from user.admin import admin_site
from vendor.models import VendorUser
from hospital.models import HospitalUser
from django.contrib import messages
from django.shortcuts import redirect, render


class VehicleAdmin(admin.ModelAdmin):
    list_display_links = None
    change_list_template = "admin/vehicle/change_list.html"
    form = CustomUserCreationForm
    model = Vehicle
    list_display = ('vehicle_no', 'User', 'type',
                    'category_name', 'mileage', 'status', 'Action')
    list_filter = ('status',)
    list_per_page = 5

    search_fields = ('vehicle_no', 'status')
    ordering = ('vehicle_no',)

    def type(sef, obj):
        if(obj.user_type == 1):
            user_type = 'Hospital'
        else:
            user_type = 'Vendor'
        return user_type

    def User(self, obj):
        if(obj.user_type == 1):
            HospitalObj = HospitalUser.objects.get(pk=obj.user_id)
            name = HospitalObj.full_name
            link = format_html(
                '<a class="user-detail" href="/admin/hospital/hospitaluser/view/%s" title="View">%s</a>' % (obj.id, name))
        else:
            VendorObj = VendorUser.objects.get(pk=obj.user_id)
            name = VendorObj.full_name
            link = format_html(
                '<a class="user-detail" href="/admin/vendor/vendoruser/view/%s" title="View">%s</a>' % (obj.id, name))
        return link

    def has_add_permission(self, request, obj=None):
        return False

    def category_name(self, obj):
        objs = VehicleCategory.objects.filter(
            id=obj.vehicle_category_id).first()
        return objs.category_name

    def Action(self, obj):
        if(obj.status == 3):
            delete = ''
        else:
            delete = '<a class="button delete_vehicle trash-icon" title="Delete" data-id="%s" href="delete/%s"><i class="fa fa-trash" aria-hidden="true"></i></a>&nbsp;' % (
                obj.id, obj.id)

        view = '<a class="button" title="View" href="view/%s"><i class="fa fa-eye" aria-hidden="true"></i></a>&nbsp;' % (
            obj.id)
        # edit   = '<a class="button edit-icon" title="Edit" data-id="%s" href="/admin/vehicle/vehicle/%s/change/"><i class="fa fa-edit" aria-hidden="true"></i></a>' % (obj.id,obj.id)
        return format_html(view + delete)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url('^view/(?P<vehicle_id>\d+)/$', self.vehicle_view),
        ]
        return my_urls + urls

    def vehicle_view(self, request, vehicle_id):
        context_data = admin_site.each_context(request)
        context_data['data'] = Vehicle.objects.all()
        context_data['site_title'] = ugettext_lazy('Vendor')
        return TemplateResponse(request, 'admin/vehicle_view.html', context=context_data)


class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display_links = None
    change_list_template = "admin/category/change_list.html"
    form = VehicleCategoryCreationForm
    model = VehicleCategory
    list_display = ('category_name','status', 'Action')
    list_filter = ('status',)
    list_per_page = 10

    search_fields = ('category_name', 'status')
    ordering = ('-id',)

    def Action(self, obj):
        if(obj.status == 2):
            delete = ''
            edit   = ''
        else:
            edit   = '<a class="button edit-icon" title="Edit" data-id="%s" href="/admin/vehicle/vehiclecategory/%s/change/"><i class="fa fa-edit" aria-hidden="true"></i></a>' % (obj.id,obj.id)
            delete = '<a class="button delete_category trash-icon" title="Delete" data-id="%s" href="delete/%s"><i class="fa fa-trash" aria-hidden="true"></i></a>&nbsp;' % (
                obj.id, obj.id)

        view = '<a class="button" title="View" href="view/%s"><i class="fa fa-eye" aria-hidden="true"></i></a>&nbsp;' % (
            obj.id)
        return format_html(view + delete + edit)

admin_site.register(Vehicle, VehicleAdmin)
admin_site.register(VehicleCategory, VehicleCategoryAdmin)