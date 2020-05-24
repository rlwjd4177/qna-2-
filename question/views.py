from django.shortcuts import render,get_object_or_404,redirect
from .models import Question
from django.utils import timezone

def home(request):
    questions = Question.objects.all()
    return render(request,'home.html',{'questions': questions})

def question(request,question_id):
    questions = get_object_or_404(Question,pk = question_id)
    return render(request,'question.html',{'question':questions})


# Create your views here.

