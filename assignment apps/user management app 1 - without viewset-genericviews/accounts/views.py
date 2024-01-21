from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *

class AdminView(APIView):
    def get(self, reqeust):
        user_obj = User.objects.all()
        serializer = AdminSerializer(user_obj, many=True)
        return Response({"data":serializer.data})
    
    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"record saved!"})
        else:
            return Response({"message":"record not saved! Try Again!"})
    
    def put(self, request, pk=None , format=None):
        if User.objects.filter(id=pk).exists():
            user_obj = User.objects.get(id=pk)
            serializer = AdminSerializer(user_obj,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message":"record updated!"})
            else:
                return Response({"message":"record not updated!"})
        else:
            return Response({"message":"user id not exist!"})

    def delete(self, request, pk=None , format=None):
        if User.objects.filter(id=pk).exists():
            user_obj = User.objects.get(id=pk)
            if user_obj.delete():
                return Response({"message":"record deleted!"})
            else:
                return Response({"message":"record not deleted!"})
        else:
            return Response({"message":"user id not exist!"})        
            
