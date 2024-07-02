from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,'index.html')
    #return HttpResponse("welcome home rahul..")
    

def About(request):
    return HttpResponse("welcome to About rahul")

def Contact(request):
    return HttpResponse("this is contact of rahul..")