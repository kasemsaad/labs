from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def heloo(request):
    retur    return HttpResponse('<h1>heloo</h1>')