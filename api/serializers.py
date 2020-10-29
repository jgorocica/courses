# Models 
from django.contrib.auth.models import User
from .models import (Courses, Lessons, 
                    Questions, Answers, 
                    RelationStudentsLessons)

# Rest framework tools
from rest_framework import serializers

from django.http import JsonResponse


class LessonSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(
        many=False,
    )

    class Meta: 
        model = Lessons
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    professor = serializers.StringRelatedField(
        many=False,
    )
    
    students = serializers.StringRelatedField(
        many=True
    )

    lessons = LessonSerializer(
        many=True, 
        read_only=True
    )
    

    class Meta: 
        model = Courses
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    question_type = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=False)

    class Meta: 
        model = Questions
        fields = ('pk', 'title', 'question_type', 'lesson', 'answers_set')

    def get_question_type(self, obj):
        return obj.get_question_type_display()


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False)

    class Meta: 
        model = Answers
        fields = ('title', 'question', 'is_correct', 'created_at')


class LessonEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'


class LessonTakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationStudentsLessons
        fields = '__all__'