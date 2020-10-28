# Django tools
from django.shortcuts import render

# Models 
from .models import Courses, Lessons, Questions

# Serializers
from .serializers import CourseSerializer, LessonSerializer, QuestionSerializer

# Rest Framework tools
from rest_framework.decorators import action
from rest_framework import viewsets, permissions




class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all().order_by('-created_at')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def lessons(self, request, *args, **kwargs):
        course = self.get_object()
        return Response(course)



class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all().order_by('-created_at')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]