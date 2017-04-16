from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request):
    q_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('thePoll/index.html')
    context = {'latest_question_list': q_list} 
    return render(request, 'thePoll/index.html', context)
#render() gets the request,  a path to the template, and the "context" (this is just to tie variables in the template to the Python objects.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'thePoll/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)

def vote(request, question_id):
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)
