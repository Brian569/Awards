from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    bio = models.CharField(max_length = 300,blank = True,default = 'Awesome Bio Will Appear Here')
    profile_pic = CloudinaryField(blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

        post_save.connect(create_profile, sender=User)

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile


class Posts(models.Model):
    project_name = models.CharField(max_length=100)
    descrition = models.CharField(max_length=500)
    project_link = models.CharField(max_length=200)
    project_image = CloudinaryField(blank=True)
    user_prof = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.project_name