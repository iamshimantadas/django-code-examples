from django.urls import path
from .views import *

urlpatterns = [
    path("",Home),
    path("suggestion/",Suggestions,name="suggestion"),
]