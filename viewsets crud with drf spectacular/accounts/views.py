from django.shortcuts import get_object_or_404, render
from core.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class UserList(viewsets.ViewSet):
    serializer_class = UserSerializer
    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        userid = pk
        if userid:
            user = get_object_or_404(queryset, pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"user id not exist for fetinging data!"})
    
    def create(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"user account created!"},status=status.HTTP_201_CREATED)
            else:
                return Response({"user account not created!"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error occured!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"user account updated!"},status=status.HTTP_201_CREATED)
            else:
                return Response({"user account not updated!"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error occured!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            if user.delete():
                return Response({"account deleted!"})
            else:
                return Response({"account not deleted!"})
        except Exception as e:
            print(e)
            return Response({"error occured!"})        
    