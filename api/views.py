# Django tools
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Models 
from .models import (Courses, Lessons, Questions, Answers, 
                    RelationStudentsCourses, RelationStudentsLessons, 
                    Students)

# Serializers
from .serializers import (CourseSerializer, LessonSerializer, 
                            QuestionSerializer, AnswerSerializer, 
                            LessonEnrollSerializer, LessonTakeSerializer)

# Rest Framework tools
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

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


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all().order_by('-created_at')
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def get_question(self, request):
        answers = Answers.objects.filter(question__pk=1)


"""
Params: 
* lesson_student_id (Relation between student and lesson) 
* answers_id 
* questions_id 
"""
class LessonTakeViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LessonTakeSerializer
    queryset = RelationStudentsLessons.objects.all()

    def post(self, request, pk): 
        data = request.data
        total_score = 0
        
        lesson_student_instance = get_object_or_404(RelationStudentsLessons, 
                                pk=data["lesson_student_id"])
        answers = Answers.objects.filter(pk__in=data["answers_id"])
        questions = Questions.objects.filter(pk__in=data["questions_id"]) 

        for q in questions: 
            for a in answers:
                if a.question == q and a.is_correct: 
                    total_score += float(q.score)
                
        if total_score >= lesson_student_instance.lesson.approval_score: 
            response = {'success': 'LESSON was approved! 😄'}
            lesson_student_instance.student_score = total_score
            lesson_student_instance.approved = True
        else: 
            response = {'success': 'LESSON was not approved, not enough score 😢'}
            lesson_student_instance.student_score = total_score
        lesson_student_instance.save()

        return Response(data=response, status=200)
        

"""
Params: 
* lesson_id 
* student_id 
"""
class LessonEnrollViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LessonEnrollSerializer
    queryset = Lessons.objects.all()

    def post(self, request, pk):
        lesson = get_object_or_404(Lessons, pk=pk)
        data = request.data

        if "lesson_id" not in data or "student_id" not in data: 
            return Response(data={'error': 'Error: No data were provied! 😢'}, status=404)

        obj_to_save = RelationStudentsLessons()
        obj_to_save.student = get_object_or_404( Students,  pk=data["student_id"])
        obj_to_save.lesson = lesson 
        obj_to_save.save() 

        response = {'success': 'Success: LESSON was enrolled! 😄'}
                

        return Response(data=response, status=200)


        

       



