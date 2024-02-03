from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import *
from .models import Class
# Create your views here.
# homepage
def index(request):
    if request.user.username:
        classList = Class.objects.filter(userID = request.user.username)
        GPA = 0.0
        for i in classList:
            if i.letterGrade == "A":
                grade = 4.0
            elif i.letterGrade == "A-":
                grade = 3.7
            elif i.letterGrade == "B+":
                grade = 3.3
            elif i.letterGrade == "B":
                grade = 3.0
            elif i.letterGrade == "B-":
                grade = 2.7
            elif i.letterGrade == "C+":
                grade = 2.3
            elif i.letterGrade == "C":
                grade = 2.0
            elif i.letterGrade == "C-":
                grade = 1.7
            elif i.letterGrade == "D+":
                grade = 1.3
            elif i.letterGrade == "D":
                grade = 1.0
            elif i.letterGrade == "F":
                grade = 0.0
            GPA = GPA + grade
        if GPA != 0:
            GPA = GPA/len(classList)
            GPA = "{:.2f}".format(GPA)
        return render(request, 'index.html', {'classList' : classList, 'unweightedGPA':GPA})
    else:
        return redirect('login')

# class adding
def addCourse(request):
    if request.method == "POST":
        add = Class(userID=request.user.username, name=request.POST.get("name"), letterGrade=request.POST.get("letterGrade"))
        add.save()
        return redirect('index')
    else:
        form = ClassForm()
        return render(request, 'addcourse.html', {'form':form})
# delete classes
def deletecourse(request):
    if request.method == "POST":
        rm = Class.objects.get(userID = request.user.username, name= request.POST.get("name"))
        rm.delete()
        return redirect("index")
    else:
        classList = Class.objects.filter(userID = request.user.username)
        return render(request, 'deleteclass.html', {'classList':classList})
    
# update classes
def updatecourse(request):
    if request.method == "POST":
        upd = Class.objects.filter(userID = request.user.username, name = request.POST.get("name"))
        upd.update(letterGrade = request.POST.get("grade"))
        print(upd.letterGrade)
        return redirect("index")
    else:
        classList = Class.objects.filter(userID = request.user.username)
        return render(request, 'editgrades.html', {'classList':classList})
        
# registration
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
