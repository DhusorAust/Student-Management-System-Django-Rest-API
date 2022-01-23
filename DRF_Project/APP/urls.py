from django import views
from django.urls import path,include

import APP


from .views import  StudentViewSet , TeacherViewSet 

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('student', StudentViewSet, basename='student')

router.register('teacher', TeacherViewSet, basename='teacher')


urlpatterns = [
    
    
    path('', include(router.urls)),
    
    # path('', include('rest_framework.urls',
                    
    #                 namespace='rest_framework')),

]


