from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    return render(request, "hello/index.html")

def joe(request):
    return HttpResponse("Hello, Joe!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        # this is the context, all the variables passed to the template
        "name": name.capitalize()
    })
