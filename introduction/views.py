from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


def index(request):
    
    return render(request, "introduction/index.html")
