from django.shortcuts import render
from django.http import *

# Create your views here.

def home_page_view(request):
    return HttpResponse("Hello World!")


def first_page_view(request):
    return HttpResponse("First View Page")


def first_page_view(request):
    return HttpResponse("First View Page")
