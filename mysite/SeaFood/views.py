from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def seaFood(request):
    return HttpResponse("SeaFood from saintmartin")
