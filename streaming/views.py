from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Movie, UserProfile
from .forms import RegistrationForm,LoginForm


def home(request):
    if request.user.is_authenticated:
        movies=Movie.objects.all()
        return render(request,'home.html',{'movies':movies})
    return redirect('login')

@login_required
def movie_detail(request,movie_id):
    movie=get_object_or_404(Movie,id=movie_id)
    return render(request,'movie_detail.html',{'movie':movie})

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,'register.html',{'form':form})
def login_view(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})   

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



