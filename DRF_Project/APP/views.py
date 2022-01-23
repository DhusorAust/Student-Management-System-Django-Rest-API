import imp
from pickle import OBJ
from unicodedata import name
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView

from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from rest_framework.permissions import AllowAny

from .models import *
from .serializer import *



from rest_framework import viewsets





class StudentViewSet(viewsets.ModelViewSet):
    
    queryset=StudentInformation.objects.all()
    
    serializer_class= StudentInfomationSerializer
    
    
    def list(self, request):
        pass

    def create(self, request):
        
        data=request.data
        
        student=StudentInformation.objects.create(
            name=data['name'],
            teacher=TeacherInformation.objects.get(pk=data['teacher']),
            email=data['email'],
            age=data['age'],
            phone=data['phone'],
            department=data['department'],
            roll=data['roll']
        
            
        )
        
        
        student.save()
        
        return Response("Created")
        
        

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass





class TeacherViewSet(viewsets.ModelViewSet):
    
    queryset=TeacherInformation.objects.all()
    
    serializer_class= TeacherInfomationSerializer
    
    
    








# class StudentDatabaseAPIView(APIView):
    
#     permission_class=[AllowAny,]
    
#     def post(self,request):
        

#         serializer=StudentInfomationSerializer(data=request.data)
        
#         if serializer.is_valid():
            
#             serializer.save()
            
#             return Response("Student Informations Saved Into Database")
    
#     def get(self,request):
        
#         queryset=StudentInformation.objects.all()
        
#         serializer=StudentInfomationSerializer(queryset,many=True)
        
#         return Response(serializer.data)
        
        


# class StudentDatabaseCrudAPIView(APIView):
    
#     def get_object(self, pk):
#         try:
#             return StudentInformation.objects.get(pk=pk)
#         except StudentInformation.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         id = self.get_object(pk)
#         serializer = StudentInfomationSerializer(id)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         id = self.get_object(pk)
#         serializer = StudentInfomationSerializer(id, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         id = self.get_object(pk)
#         id.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    

