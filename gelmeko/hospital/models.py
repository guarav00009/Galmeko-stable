from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class HospitalUser(models.Model):
    full_name = models.CharField(max_length=50,blank=False,null=False)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50,blank=False,null=False)
    password = models.CharField(max_length=100,null=False)
    is_active = models.BooleanField(default=True)
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Active'),
        (2, 'Rejected'),
        (3, 'Deleted'),
    )
    status = models.IntegerField(
        _('status'), choices=STATUS_CHOICES, default=0)
    is_email_verified = models.BooleanField(
        _('is email verified'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(_('deteted at'), blank=True, null=True)
    deleted_by_id = models.IntegerField(_('deteted by'), blank=True, null=True)

    class Meta:
        verbose_name = 'Hospital User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.full_name