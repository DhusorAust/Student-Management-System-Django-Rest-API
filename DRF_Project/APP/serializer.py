from dataclasses import field
from .models import *

from rest_framework import serializers






        
        
class StudentInfomationSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        
        model=StudentInformation
        
        fields ='__all__'


class TeacherInfomationSerializer(serializers.ModelSerializer):
    
    students=StudentInfomationSerializer(many=True)
    
    class Meta:
        
        model=TeacherInformation
        
        fields ='__all__'
        
