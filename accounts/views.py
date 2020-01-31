from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password1'])
        if user is not None:
            auth.login(request, user)
            return redirect('add')
        else:
                return render(request, 'login.html', {"error":"Username or Password is invalid"})

    else:
        return render(request, 'login.html')
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirmPassword']:
            try:
                user= User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error':'Username has Been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password'])
                addInfo = Profile(username = user, email = request.POST["email"], currentGrade = request.POST["currentGrade"],contactNo = request.POST["contactno"])
                auth.login(request, user)
                return redirect('add')
        else:
            return render(request, 'signup.html', {'error':'Password doesnt match'})
    else:
        return render(request, 'signup.html')
@login_required
def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
@login_required
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'profile.html', {'user':user})
