from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def simple_home(request):
    return HttpResponse("<h1>Travel Tribe is Working!</h1><p>Your Django app is running on Render!</p>")

def health_check(request):
    return JsonResponse({'status': 'healthy', 'message': 'Django is working'})

def simple_test(request):
    return HttpResponse("OK - Server is running!")