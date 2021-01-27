from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(self):
    return HttpResponse("Helllo!")
