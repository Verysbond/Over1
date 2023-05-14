from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 2 + 3
    return render(request, 'about.html', {'gretting': a})


def home(request):
    return render(request, 'home.html')
