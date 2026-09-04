from django.shortcuts import render
from django.http import HttpRequest

def ashwini(request):
    return render(request,"landingpages/index.html")