from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    content = '<h1 style="color:red">Welcome to the Homepage</h1>'
    return HttpResponse(content)