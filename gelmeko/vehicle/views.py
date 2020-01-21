from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
import json

def delete_page_view(request):
    result = {}
    if request.method == 'POST' and request.is_ajax():
        try:
            print('okkkkkkkkkkkkkkkkk')
        except KeyError as e:
            return JsonResponse(str(e))
    else:
        return render(request, 'admin/dashboard.html', {})