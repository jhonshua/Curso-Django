# from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import  render
from .models import Project, Task

# Create your views here.


def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'fazt'
    return render(request, 'about.html', {
        'username': username
    })
    
def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    return render(request,'tasks.html')


