from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 2 + 3
    return render(request, 'about.html', {'gretting': a})

def reverse(request):
    user_text = request.GET['usertext']
    reverse = user_text[::-1]
    return render(request, 'reverse.html', {'word': reverse})


def home(request):
    return render(request, 'home.html')
