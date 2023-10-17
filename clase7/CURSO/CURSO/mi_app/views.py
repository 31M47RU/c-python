from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello World bla bla bla ! ")


def return_file(request):
    return render(request, "hello.html")


def return_dynamic_file(request):
    return render(request, "hello-dynamic.html", {"name": "Juan", "age": 30})
