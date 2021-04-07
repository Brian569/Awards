from django import forms
from .models import Posts, Profile

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']
        exclude = ['user']

class UploadProjects(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['project_name', 'descrition', 'project_link', 'project_image']
        exclude = ['user_prof']