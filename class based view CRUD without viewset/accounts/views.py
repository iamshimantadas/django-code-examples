
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Student
from .serializer import StudentSerializer


class StudentList(APIView):
    def get(self, request, pk=None):
        userid = pk
        if userid:
            if Student.objects.filter(id=userid).exists():
                stu_obj = Student.objects.get(id=userid)
                serializer = StudentSerializer(stu_obj)
                return Response({"data": serializer.data})
            else:
                return Response({"user id not exist!"})
        else:
            user = Student.objects.all()
            serializer = StudentSerializer(user, many=True)
            return Response({"data": serializer.data})

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"account created!"})
        else:
            return Response({"account not created!"})

    def put(self, request, pk=None, format=None):
        if Student.objects.filter(id=pk).exists():
            stu_obj = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu_obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"account updated!"})
            else:
                return Response({"account not created!"})
        else:
            return Response({"user id not exist!"})
        
    def delete(self, request, pk=None):
        userid = pk
        if Student.objects.filter(id=userid).exists():
            stu_obj = Student.objects.get(id=userid)
            if stu_obj.delete():
                return Response({"account deleted!"})
            else:
                return Response({"account not deleted!"})
        else:
            return Response({"user id not exist!"})    
             
