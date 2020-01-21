from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class VehicleCategory(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    STATUS_CHOICES = (
        (1, 'Active'),
        (0, 'Inactive'),
        (2, 'Deleted'),
    )
    status = models.IntegerField(
        _('status'), choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vehicle_category"
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.category_name

class Vehicle(models.Model):
    user_id = models.IntegerField()
    vehicle_category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=25,unique=True)
    mileage = models.CharField(max_length=11,blank=False,null=False)
    STATUS_CHOICES = (
        (1, 'Hospital'),
        (2, 'Vendor'),
    )
    user_type = models.IntegerField(
        _('user_type'), choices=STATUS_CHOICES, default=1)
    STATUS_CHOICES = (
        (1, 'Active'),
        (0, 'Inactive'),
        (2, 'Booked'),
        (3, 'Deleted'),

    )
    status = models.IntegerField(
        _('status'), choices=STATUS_CHOICES, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(_('deteted at'), blank=True, null=True)
    deleted_by_id = models.IntegerField(_('deteted by'), blank=True, null=True)

    class Meta:
        db_table = "vehicle"

    def __str__(self):
        return self.vehicle_no

