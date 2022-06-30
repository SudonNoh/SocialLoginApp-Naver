from django.urls import path, include
from user.API.views import (
    NaverLoginAPIView, NaverCallbackAPIView, NaverToDjangoLoginView
    )

urlpatterns = [
    path('naver/login', NaverLoginAPIView.as_view()),
    path('naver/callback', NaverCallbackAPIView.as_view()),
    path('naver/login/success', NaverToDjangoLoginView.as_view()),
]
