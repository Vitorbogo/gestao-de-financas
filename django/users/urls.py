from django.urls import path

from users.views import UserProfileView, UserLoginAPIView, UserCreateView


urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('user/', UserProfileView.as_view()),
    path('create/user/', UserCreateView.as_view()),
]
