from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from  django.template import loader
# Create your views here.
def index(req):
    latest_quesiton_list = Question.objects.order_by('-pub_date')[0:10]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_quesiton_list
    }
    #return HttpResponse(template.render(context,req))
    return render(req,'polls/index.html', context)

def detail(req,qid):
    try:
        question = Question.objects.get(pk=qid)
        # for choice in question.choice_set.all():
        #     print(choice.choice_set)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(req,'polls/detail.html',{'question':question})


def results(req,qid):
    return HttpResponse("You're looking at results of the question %s." % qid)

def vote(req,qid):
    return HttpResponse("You're voting on question %s." % qid)