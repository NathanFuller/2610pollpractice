from django.http import HttpResponse

def index(request):
    return HttpResponse("Hweolrllod")

def detail(request, question_id):
    return HttpResponse("Question #%s" % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)

def vote(request, question_id):
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)
