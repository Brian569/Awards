from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UpdateProfileForm, UploadProjectsForm, ReviewProjectForm
from django.contrib.auth import logout
from django.contrib import messages


@login_required
def projects(request):
    project = Posts.get_post()
    

    return render(request, 'projects.html', {'project': project})
@login_required
def home(request):
    project = Posts.get_post()
    

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
            form = UpdateProfileForm(request.POST, request.FILES, instance= Profile.objects.get(user_id = current_user))

        else:
            form = UpdateProfileForm(request.POST, request.FILES)
            
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = current_user
            user_profile.save()
            
            return redirect('profile', current_user.id)
    else:
        if Profile.objects.filter(user_id = current_user).exists():
            form = UpdateProfileForm(instance = Profile.objects.get(user_id = current_user))
        else:
            form = UpdateProfileForm()

    return render(request, 'update_profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def upload(request):

    current_user = request.user
    profile = Profile.objects.get(user= request.user.id)

    if request.method == 'POST':
        form = UploadProjectsForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=True)
            project.profile = current_user
            project.user_prof = profile
            project.save()
            print('Saved')

            return redirect('home')

    else:
        form = UploadProjectsForm()

    return render(request, 'upload.html', {'form': form})

@login_required
def reviews(request, pk):
   
    project = get_object_or_404(Posts, pk=pk)
    review = Review.objects.all()

    current_user = request.user
    if request.method == 'POST':
        form = ReviewProjectForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            comment = form.cleaned_data['comment']
            review = form.save(commit=False)
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.save()

            # print('saves',review)
            return redirect('projects')

    else:
        form = ReviewProjectForm()
        
    return render(request, 'review.html', {'form' : form, 'user': current_user})

@login_required
def single(request, post_id):

    posts = Posts.objects.filter(pk=post_id)
    reviews  = Review.get_review()

  
    
    return render(request, 'single.html', {'reviews': reviews, 'posts': posts})

@login_required
def search(request):
    if 'post' in request.GET and request.GET['post']:
        tearm = request.GET.get('post')
        searched = Posts.find(tearm)
        message = f" {tearm} "

        return render(request, 'search.html', {'message': message, 'posts' : searched})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
