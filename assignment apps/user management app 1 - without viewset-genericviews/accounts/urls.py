from django.urls import path
from .views import *

urlpatterns = [
path('admins/',AdminView.as_view()),
]