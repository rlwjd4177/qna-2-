from django.shortcuts import render,get_object_or_404,redirect

import pdb
from .models import Answer



def select(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = answer.question
    
    # q_user = question.user
    # if q_user.point < 10:
    #     q_user.point -= 10
    #     answer.user.point += 10
    #     q_user.save()
    #     answer.user.save()   
    

    answer.selected = True
    answer.save()
    
    return redirect('question', question.id)


def new(request):
    return render(request,'answer.html')



def create(request,answer_id):
    new_answer = Answer()
    new_answer.title = request.POST['title']
    new_answer.body = request.POST['body']
    return redirect('answer')
    # answer -> question 구동 확인되면 바꾸기