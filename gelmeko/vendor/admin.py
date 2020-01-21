from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.html import format_html
from vendor.models import VendorUser
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from user.admin import admin_site


class VendorUserAdmin(admin.ModelAdmin):
    list_display_links = None
    change_list_template = 'admin/vendor/change_list.html'
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = VendorUser 
    list_display = ('full_name', 'email', 'company_name',
                    'phone', 'status', 'Action')
    list_filter = ('status',)
    list_per_page = 5  # For Pagination
    fieldsets = (
        (None, {'fields': ('full_name', 'email',
                           'company_name', 'phone', 'password', 'status')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'company_name', 'phone', 'password', 'is_active', 'status')}
         ),
    )
    search_fields = ('email', 'full_name')
    ordering = ('full_name',)

    def Action(self, obj):
        if(obj.status == 3):
            delete = ''
            edit   = ''
        else: 
            delete = '<a class="button delete_vendor_user trash-icon" title="Delete" data-id="%s" href="delete/%s"><i class="fa fa-trash" aria-hidden="true"></i></a>&nbsp;' % (
                obj.id, obj.id)
            edit   = '<a class="button edit-icon" title="Edit" data-id="%s" href="/admin/vendor/vendoruser/%s/change/"><i class="fa fa-edit" aria-hidden="true"></i></a>' % (obj.id,obj.id)


        view = '<a class="button" title="View" href="view/%s"><i class="fa fa-eye" aria-hidden="true"></i></a>&nbsp;' % (
            obj.id)
        return format_html(view + delete + edit)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url('^view/(?P<vendor_id>\d+)/$', self.vendor_view),
        ]
        return my_urls + urls

    def vendor_view(self, request, vendor_id):
        context_data = admin_site.each_context(request)
        context_data['data'] = VendorUser.objects.all()
        context_data['site_title'] = ugettext_lazy('Vendor')
        return TemplateResponse(request, 'admin/vendor_view.html', context=context_data)


admin_site.register(VendorUser, VendorUserAdmin)
