from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from cms.models import Pages
# Create your views here.

def annotated(request):
    answer = ""
    user = ""
    if request.user.is_authenticated():
        user = request.user.username
        if request.method == "GET" :
            template = get_template('annotated.html')
        elif request.method == "PUT" or request.method == "POST":
            try:
                split_list = request.body.split('&', 2)
                name = split_list[1].split('=')[1]
                content = split_list[2].split('=')[1]
            except IndexError:
                print("eh! ha petado :)")
            if name != "" and content != "":
                database = Pages(name=name, page=content)
                database.save()
            else:
                return HttpResponse("Empty QS")
            template = get_template('annotated.html')
    else:
        template = get_template("unlogged.html")
    context = RequestContext(request, {"user" : user, "answer" : answer})
    return HttpResponse(template.render(context))

def redirect(request):
    template = get_template('annotated.html')
    return HttpResponseRedirect("http://localhost:8000/annotated/pages/")
