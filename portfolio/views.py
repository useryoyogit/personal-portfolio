from os import execv
from django.http import Http404
from django.shortcuts import render
from .models import Project, SocialAcc, Skill


def home(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {
        'skills': skills
    })


def works(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/works.html', {
        'projects': projects
    })


def contact(request):
    accounts = SocialAcc.objects.all()
    return render(request, 'portfolio/contact.html', {
        'accounts': accounts
    })
