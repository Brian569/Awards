from django import forms
from .models import *

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']
        exclude = ['user']