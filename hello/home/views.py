from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context ={
        "variable": "can be useful"
    }
    return render(request, 'index.html',context)
    #  return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is Services page")

def contact(request):
    return HttpResponse("this is Contact page")

def Saurav(request):
    return HttpResponse("you are welcome") 