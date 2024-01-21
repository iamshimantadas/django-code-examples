from django.urls import path

from .views import *

urlpatterns = [
    path('auth/',StudentList.as_view()),
    path('auth/<int:pk>',StudentList.as_view()),
]