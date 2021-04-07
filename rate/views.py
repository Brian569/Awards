from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UpdateProfile, UploadProjects
from django.contrib.auth import logout

@login_required
def home(request):
    project = Posts.objects.all()

    return render(request, 'home.html', {'project': project})

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

@login_required
def upload(request):

    current_user = request.user
    profile = Profile.objects.get(user= request.user.id)

    if request.method == 'POST':
        form = UploadProjects(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=True)
            project.profile = current_user
            project.user_prof = profile
            project.save()
            print('Saved')

            return redirect('home')

    else:
        form = UploadProjects()

    return render(request, 'upload.html', {'form': form})