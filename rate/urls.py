from django.urls import path, re_path
from .views import (
    home, profile,
    updateProfile,
    logout_view, upload,
    reviews, single, search
    )

urlpatterns = [
    path('', home, name='home'),
    re_path('profile/(\d+)', profile, name='profile'),
    path('update/', updateProfile, name = 'updateProfile'),
    path('logout/', logout_view, name='logouts'),
    path('uplaod/', upload, name = 'upload'),
    re_path('reviews/(\d+)', reviews, name = 'reviews'),
    re_path('single/(\d+)', single, name = 'single'),
    path('search/', search, name = 'search'),
]