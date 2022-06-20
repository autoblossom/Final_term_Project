from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question




def index(request):
    template = loader.get_template("introduction/index.html")
    context ={
    }
    return HttpResponse(template.render(context,request))

def detail(req,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exist")
    return render(req,'polls/detail.html',{'question':question})
