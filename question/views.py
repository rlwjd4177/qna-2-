from django.shortcuts import render,get_object_or_404,redirect
from .forms import QuestionForm
from .models import Question
from django.utils import timezone

def home(request):
    questions = Question.objects.all()
    return render(request,'home.html',{'questions': questions})

def question(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    answers = Answer.objects.filter(question_id = question.id)
    return render(request,'question.html',{'question':question, 'answers': answers})


def search(request):
    q = request.GET.get('q')

    questions = Question.objects.filter(
            title__icontains=q
        ) | Question.objects.filter(
            body__icontains=q
        ) | Question.objects.filter(
            professor_name__icontains=q
        )
    """
    answers = Answer.objects.filter(
            title__icontains=q
        ) | Answer.objects.filter(
            body__icontains=q
    )"""

    return render(request,'search.html',{'questions':questions})

def new(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid :
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('question',content.id)
    else :
        form = QuestionForm()
        return render(request,'new.html',{'form':form})


# Create your views here.

