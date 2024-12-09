# from django.shortcuts import render
from  django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    return HttpResponse("<h1>Index page<h1>")
    
def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)
   
def about(request):
   return HttpResponse('<h1>About<h1>')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe = False)

def tasks(request, title):
    task = get_object_or_404(Task, title = title)
    return HttpResponse('Task: %s' % task.title)


