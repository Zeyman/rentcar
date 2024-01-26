from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rentcar.models import Car
import json

# Create your views here.
a = { 
    "name":"John", 
    "age":30, 
    "car":"Volvo" 
}

b= [1,3]

def showcar(request):
	return HttpResponse('This is the list of cars');

def jsotest(request):
	return JsonResponse(a)

#def list(request):
#    data = Car.objects.
#    #json_data = json.dumps(list(data))
#    return JsonResponse(list(data))