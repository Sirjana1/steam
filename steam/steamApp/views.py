# yourapp/views.py
from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse("Hello,")
