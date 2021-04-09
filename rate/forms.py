from django import forms
from .models import Posts, Profile, Review


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'email', 'phone_number']
        exclude = ['user']

class UploadProjectsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['project_name', 'description', 'project_link', 'project_image']
        exclude = ['user_prof']

class ReviewProjectForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = ['design', 'content', 'usability', 'comment']
        exclude = ['project', 'user']