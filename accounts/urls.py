from django.urls import path
from .views import SignUpView, ProfilesListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profilesList/', ProfilesListView.as_view(), name='profilesList'),
]