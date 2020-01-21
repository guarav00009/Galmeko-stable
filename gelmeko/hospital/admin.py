from django.contrib import admin
from .forms import CustomUserCreationForm
from django.utils.html import format_html
from hospital.models import HospitalUser
from vehicle.models import VehicleCategory
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from user.admin import admin_site
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HospitalUserAdmin(admin.ModelAdmin):
    list_display_links = None
    change_form_template = 'admin/hospital/change_form.html'
    change_list_template = 'admin/hospital/change_list.html'
    form = CustomUserCreationForm
    model = HospitalUser
    list_display = ('full_name','email', 'phone','address','status','Action')
    list_filter = ('status',)
    list_per_page = 5   #For Pagination

    fieldsets = (
        (None, {'fields': ('full_name','email','phone','address','status','password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','email','phone','status','password', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('-id',)
    
    def Action(self, obj):
        if(obj.status == 3):
            delete = ''
            edit   = ''
        else: 
            delete = '<a class="button delete_hospital_user trash-icon" title="Delete" data-id="%s" href="delete/%s"><i class="fa fa-trash" aria-hidden="true"></i></a>&nbsp;' % (
                obj.id, obj.id)
            edit   = '<a class="button edit-icon" title="Edit" data-id="%s" href="/admin/hospital/hospitaluser/%s/change/"><i class="fa fa-edit" aria-hidden="true"></i></a>' % (obj.id,obj.id)

        view = '<a class="button" title="View" href="view/%s"><i class="fa fa-eye" aria-hidden="true"></i></a>&nbsp;' % (
            obj.id)
        add = '<a class="button" title="Add Vehicle" href="add_vehicle/%s"><i class="fa fa-plus" aria-hidden="true"></i></a>&nbsp;' % (
            obj.id)
        return format_html(view + delete + edit + add)
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url('^view/(?P<hospital_id>\d+)/$', self.hospital_view),
            url('^add_vehicle/(?P<hospital_id>\d+)/$', self.vehicle_add),
        ]
        return my_urls + urls

    @method_decorator(login_required())
    def vehicle_add(self, request,hospital_id):
        context_data = admin_site.each_context(request)
        context_data['data'] = HospitalUser.objects.get(id=hospital_id)
        context_data['category'] = VehicleCategory.objects.all()
        context_data['site_title'] = ugettext_lazy('Hospital')
        return TemplateResponse(request, 'admin/hospital/add_vehicle.html', context=context_data)

    def hospital_view(self, request,hospital_id):
        context_data = admin_site.each_context(request)
        context_data['data'] = HospitalUser.objects.get(id=hospital_id)
        context_data['site_title'] = ugettext_lazy('Hospital')
        return TemplateResponse(request, 'admin/hospital_view.html', context=context_data)

admin_site.register(HospitalUser,HospitalUserAdmin)
