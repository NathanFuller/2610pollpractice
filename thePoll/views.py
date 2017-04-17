from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from .models import Question, Choice

def index(request):
    q_list = Question.objects.order_by('-pub_date')
    #template = loader.get_template('thePoll/index.html')
    context = {'latest_question_list': q_list} 
    return render(request, 'thePoll/index.html', context)
#render() gets the request,  a path to the template, and the "context" (this is just to tie variables in the template to the Python objects.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'thePoll/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'thePoll/results.html', {'question':question}) 

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'thePoll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
	selected_choice.save()
        return HttpResponseRedirect(reverse('thePoll:results', args=(question.id,)))
