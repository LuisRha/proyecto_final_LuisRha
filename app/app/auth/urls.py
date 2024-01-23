from django.urls import path

from ..auth.user.api.user_views import UserLoginAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]
