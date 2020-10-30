# Views 
from .views import (CourseViewSet, LessonViewSet, QuestionViewSet, 
                    AnswerViewSet, LessonEnrollViewSet, LessonTakeViewSet)

# Rest framework tools
from rest_framework.routers import DefaultRouter

# Tools 
from django.urls import path, include


router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('lessons/<int:pk>/enroll', LessonEnrollViewSet.as_view(), name='lesson_enroll'),
    path('lessons/<int:pk>/take', LessonTakeViewSet.as_view(), name='lesson_take')

]