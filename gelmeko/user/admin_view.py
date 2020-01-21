from django.http import HttpResponse, Http404,JsonResponse,HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from vehicle.models import Vehicle,VehicleCategory
from hospital.models import HospitalUser
from vendor.models import VendorUser
from django.contrib import messages
import json
def vehicle_soft_delete(request): 
    result = {}
    if request.method == 'POST' and request.is_ajax():      
        try:
            vehicleId = request.POST.get('id', '')
            response = Vehicle.objects.filter(pk=vehicleId).update(status=3)
            if (response == True):
                result['status'] = True
                result['msg'] = 'Vehicle Deleted Successfully successfully!'
                return JsonResponse(result)
            else:
                result['status'] = False
                result['msg'] = 'Something went wrong!'
                return JsonResponse(result)
        except Http404:
            return HttpResponseRedirect("/admin/vehicle/vehicleuser/")
    else:
        return HttpResponse('Invalid request passed')

def hospitaluser_soft_delete(request): 
    result = {}
    if request.method == 'POST' and request.is_ajax(): 
        try:
            Hospital_userId = request.POST.get('id', '')
            response = HospitalUser.objects.filter(pk=Hospital_userId).update(status=3)
            if (response == True):
                result['status'] = True
                result['msg'] = 'Hospital User Deleted Successfully successfully!'
                return JsonResponse(result)
            else:
                result['status'] = False
                result['msg'] = 'Something went wrong!'
                return JsonResponse(result)
        except Http404:
            return HttpResponseRedirect("/admin/hospital/hospitaluser/")
    else:
        return HttpResponse('Invalid request passed')

def category_soft_delete(request): 
    result = {}
    if request.method == 'POST' and request.is_ajax(): 
        try:
            categoryId = request.POST.get('id', '')
            response = VehicleCategory.objects.filter(pk=categoryId).update(status=2)
            if (response == True):
                result['status'] = True
                result['msg'] = 'Category Deleted Successfully successfully!'
                return JsonResponse(result)
            else:
                result['status'] = False
                result['msg'] = 'Something went wrong!'
                return JsonResponse(result)
        except Http404:
            return HttpResponseRedirect("/admin/vehicle/vehiclecategory/")
    else:
        return HttpResponse('Invalid request passed')

def vendoruser_soft_delete(request): 
    result = {}
    if request.method == 'POST' and request.is_ajax(): 
        try:
            vendor_id = request.POST.get('id', '')
            response = VendorUser.objects.filter(pk=vendor_id).update(status=3)
            if (response == True):
                result['status'] = True
                result['msg'] = 'Vendor User Deleted Successfully successfully!'
                return JsonResponse(result)
            else:
                result['status'] = False
                result['msg'] = 'Something went wrong!'
                return JsonResponse(result)
        except Http404:
            return HttpResponseRedirect("/admin/vendor/vendoruser/")
    else:
        return HttpResponse('Invalid request passed')

def vehicle_save(request):
    result = {}
    if request.method == 'POST': 
        try:
            vehicle_no = request.POST.getlist('vehicle_no')
            status = request.POST.getlist('status')
            mileage = request.POST.getlist('mileage')
            vehicle_category = request.POST.getlist('vehicle_category')
            user_id = request.POST.get('user_id')
            types = request.POST.get('type')
            length = min([len(vehicle_no), len(status), len(mileage), len(vehicle_category)])
            for i in range(length):
                vehicle = Vehicle(user_id= user_id,vehicle_no= vehicle_no[i],mileage= mileage[i],user_type= types,status= status[i],vehicle_category_id= vehicle_category[i]
                    )
                vehicle.save()
            if (vehicle.id):
                messages.success(request, 'Vehicle Added successfully!')
            else:
                messages.success(request, 'Something went wrong!')
            return HttpResponseRedirect("/admin/hospital/hospitaluser/")
        except Http404:
            return HttpResponseRedirect("/admin/hospital/hospitaluser/")
    else:
        return HttpResponse('Invalid request passed')
