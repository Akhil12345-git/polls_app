from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Question


def index(request):
    return HttpResponse("<p>Hello Django</p>")


def detail(request, question_id):
    return HttpResponse("You aer looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on question %s." % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



