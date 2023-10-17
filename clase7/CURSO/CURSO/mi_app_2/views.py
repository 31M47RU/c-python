from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def chau(request):
    return HttpResponse("Chau Mundo ! ")
