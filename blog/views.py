from django.shortcuts import render
from django.http import HttpResponse

#home function for user going to blog home page
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
# Create your views here.
