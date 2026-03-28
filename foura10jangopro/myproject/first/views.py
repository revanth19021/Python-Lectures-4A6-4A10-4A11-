from django.shortcuts import render
from .models import Register
# Create your views here.
from django.contrib.auth.models import User

from django.http import HttpResponse


def hai(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error':'username is already exissted'})
        
        User.objects.create(
            username=username,
            password=password,
            email=email
        )
        return render(request,'login.html')
    return render(request,'register.html')


