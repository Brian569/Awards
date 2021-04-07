from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UpdateProfile
from django.contrib.auth import logout

@login_required
def home(request):

    return render(request, 'home.html')

@login_required
def profile(request, prof_id):
    user = User.objects.filter(pk=prof_id )
    profile = Profile.objects.filter(user= prof_id)

    return render(request, 'profile.html', {"profile" : profile})

@login_required
def updateProfile(request):

    current_user = request.user
    if request.method == 'POST':
        if Profile.objects.filter(user_id = current_user).exists():
            form = UpdateProfile(request.POST, request.FILES, instance= Profile.objects.get(user_id = current_user))

        else:
            form = UpdateProfile(request.POST, request.FILES)
            
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = current_user
            user_profile.save()
            
            return redirect('profile', current_user.id)
    else:
        if Profile.objects.filter(user_id = current_user).exists():
            form = UpdateProfile(instance = Profile.objects.get(user_id = current_user))
        else:
            form = UpdateProfile()

    return render(request, 'update_profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')