from django.urls import path

from .views import *

urlpatterns = [
    path('auth/',UserList.as_view()),
    path('auth/<id>',RetriveList.as_view()),
]