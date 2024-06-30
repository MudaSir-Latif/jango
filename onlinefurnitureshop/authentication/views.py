from django.shortcuts import render

def login(request):
    return render (request,'reg/signup.html')

def signup(request):
    return render (request,'reg/login.html')
