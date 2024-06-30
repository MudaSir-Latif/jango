from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

# @login_required
def checkout(request):
    return render(request,'checkout.html')