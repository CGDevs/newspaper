from django.shortcuts import render
from django.http import HttpResponse
from models import Question, Choice

def index(request):

    question = Question.objects.all()
    context = {
        'questions':question
    }
    return render(request, 'polls/index.html', context)
