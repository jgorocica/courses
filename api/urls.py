# Views 
from .views import CourseViewSet, LessonViewSet, QuestionViewSet

# Rest framework tools
from rest_framework.routers import DefaultRouter

# Tools 
from django.urls import path, include


router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'questions', QuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]