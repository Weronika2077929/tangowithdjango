from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("This tutorial has been put together by Weronika Lachtara, 2077929 </br> Rango says here is the about page. <a href='/rango/'>Index</a>")