from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader


def index(request):
    template = loader.get_template("introduction/index.html")
    context ={
    }
    return HttpResponse(template.render(context,request))