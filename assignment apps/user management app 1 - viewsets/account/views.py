from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import User
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import *

class AccountView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, isManager]
    authentication_classes = [JWTAuthentication]


        


