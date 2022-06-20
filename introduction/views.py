from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

def index(request):
    
    return render(request, "introduction/index.html")

class Index(View):
    def get(request):
        return render(request, "main/index.html")