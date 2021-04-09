from django.test import TestCase
from .models import *

class ProfileTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='bmn')
        self.profile = Profile.objects.create(user=self.user, bio='nicely done')

    def instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def save_prof(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='bmn')
        self.profile = Profile.objects.create(user=self.user, bio='nicely done', phone_number=72329493)

        self.project = Posts.objects.create(project_name='boom', descrition='Awesome project', project_link='https://review-apk.herokuapp.com', user_prof=self.user)


    def instance(self):
        self.assertTrue(isinstance(self.project, Posts))
