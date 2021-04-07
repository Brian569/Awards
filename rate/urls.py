from django.urls import path, re_path
from .views import (
    home, profile,
    updateProfile,
    logout_view)

urlpatterns = [
    path('', home, name='home'),
    re_path('profile/(\d+)', profile, name='profile'),
    path('update/', updateProfile, name = 'updateProfile'),
    path('logout/', logout_view, name='logouts')
]