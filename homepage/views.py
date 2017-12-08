from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html')


def fun(request):
    return render(request, 'homepage/fun.html')


def projects(request):
    return render(request, 'homepage/projects.html')
