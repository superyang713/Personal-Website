from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html')


def fun(request):
    return render(request, 'homepage/fun.html')


def projects(request):
    return render(request, 'homepage/projects.html')


def instrument_design(request):
   return render(request, 'homepage/instrument_design.html')


def cluster_deposition(request):
   return render(request, 'homepage/cluster_deposition.html')


def molecular_beam(request):
   return render(request, 'homepage/molecular_beam.html')


def results(request):
   return render(request, 'homepage/results.html')
