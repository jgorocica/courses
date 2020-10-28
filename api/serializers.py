# Models 
from django.contrib.auth.models import User
from .models import Courses, Lessons, Questions

# Rest framework tools
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    professor = serializers.StringRelatedField(
        many=False,
    )
    
    students = serializers.StringRelatedField(
        many=True
    )

    lessons = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True,
        view_name='lessons-detail'
    )
    


    class Meta: 
        model = Courses
        fields = ['id', 'title', 'professor', 'students', 'lessons', 'created_at']




class LessonSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(
        many=False,
    )

    class Meta: 
        model = Lessons
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    question_type = serializers.SerializerMethodField()

    class Meta: 
        model = Questions
        fields = '__all__'

    def get_question_type(self, obj):
        return obj.get_question_type_display()