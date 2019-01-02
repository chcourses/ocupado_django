from django.contrib import admin
from django.urls import path, include
from .views import home, ProfileView, UserListView, UsersListView, ProfileEmailUpdate
urlpatterns = [
    path('', home, name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profiles/<int:pk>', UserListView.as_view(), name='profile-view'),
    path('profiles/', UsersListView.as_view(), name='profiles'),
    path('profile/email-update/', ProfileEmailUpdate.as_view(),
         name='profile-email-update'),
    path('accounts/', include('django.contrib.auth.urls')),
]
