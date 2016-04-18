from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def showPages(request):
    answer = ""
    pageList = Pages.objects.all()
    if request.user.is_authenticated():
        user = request.user.username
        template = get_template("logged.html")
    else:
        template = get_template("unlogged.html")
        user = ""
    for page in pageList:
        answer += '<li><a href="/' + str(page.id) + '">' + page.name + '</a>'
    return HttpResponse(template.render(Context({"user" : user, "message": answer})))

def insert(request, arg1, arg2):
    newPage = Pages(name=arg1, page=arg2)
    newPage.save()
    answer = "200 OK"
    return HttpResponse(answer)

def page(request, identificator):
    try:
        page = Pages.objects.get(id=identificator)
        answer = page.page
    except ObjectDoesNotExist:
        answer = "The page does not exists."
    return HttpResponse(answer)

def notFound(request):
    return HttpResponse ("NOT FOUND")
