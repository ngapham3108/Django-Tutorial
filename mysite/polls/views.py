from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from  django.template import loader
from django.urls import reverse
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
    question = get_object_or_404(Question, pk=qid)
    return render(req, 'polls/results.html', {'question': question})

def vote(req,qid):
    question = get_object_or_404(Question, pk=qid)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
