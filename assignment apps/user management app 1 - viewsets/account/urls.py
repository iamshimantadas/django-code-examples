from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("",AccountView)

urlpatterns = []

urlpatterns = urlpatterns + router.urls