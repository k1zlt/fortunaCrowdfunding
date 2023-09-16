from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

@login_required(login_url='login')
def home(request):
    return HttpResponse(request.user.username)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('authhome')
        else:
            print('*' * 80)
            print(form.errors)
            print('*' * 80)
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')

def loginuser(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect('authhome')
        else:
            return render(request, 'authentication/login.html', {'error': 'Username and password did not match'})
    else:
        return render(request, 'authentication/login.html')