from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Courses, Lessons, Questions
from .serializers import CourseSerializer, LessonSerializer, QuestionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all().order_by('-created_at')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all().order_by('-created_at')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]