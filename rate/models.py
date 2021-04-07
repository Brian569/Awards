from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    bio = models.CharField(max_length = 300,blank = True,default = 'Awesome Bio Will Appear Here')
    profile_pic = CloudinaryField(blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user