from django.urls import path
from .views import LeaveListCreateView, LeaveUpdateView
from .views_auth import register, login

urlpatterns = [
    path('register/', register),
    path('login/', login),

    path('leaves/', LeaveListCreateView.as_view()),
    path('leaves/<int:pk>/', LeaveUpdateView.as_view()),
]
