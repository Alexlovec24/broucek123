from django.shortcuts import render

from django.http import HttpResponse
import random

# Create your views here.
def models_list(request):
    random_number = random.randint(a=1,b=10)
    return HttpResponse(f"Nahodne cislo {random_number}")



