from django.urls import path, include

from .views import UserList

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('userapis', UserList, basename='user')

urlpatterns = [
    path('',include(router.urls)),
]