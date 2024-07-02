from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,'htmlcode/index.html')
    #return HttpResponse("welcome home rahul..")
    

def About(request):
    return render(request,'htmlcode/about.html')
    #return HttpResponse("welcome to About rahul")

def Contact(request):
    return render(request, 'htmlcode/contact.html')
    #return HttpResponse("this is contact of rahul..")