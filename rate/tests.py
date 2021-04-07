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