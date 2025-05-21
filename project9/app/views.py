from django.shortcuts import render
from app.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        ename = request.POST.get('ename')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        gender = request.POST.get('gender')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        emp = Employee(ename=ename, pno=pno, email=email, add=add, gender=gender, username=un, password=pw)
        emp.save()
        return HttpResponseRedirect(reverse('user_login'))
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        all_users = Employee.objects.all()
        for user in all_users:
            if user.username == un:
                if user.password == pw:
                    return HttpResponse('Logged in Successfully')
                else:
                    return HttpResponse('Invalid Password')
        else:
            return HttpResponse('user Not found')
    return render(request, 'login.html')