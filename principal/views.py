from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def principal(request):
    return render(request, 'principal.html')