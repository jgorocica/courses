# Admin tools
from django.contrib import admin

# Models 
from .models import (Professors, Students, Courses,
                    Lessons, Questions, Answers,
                    RelationStudentsCourses, RelationStudentsLessons)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'professor', 'created_at')


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'created_at')
    

class AnswersAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_question_title', 'is_correct', 'created_at')

    def get_question_title(self, obj):
        return obj.get_question_title()

    get_question_title.short_description = 'Pregunta'

class RelationStudentsCoursesAdmin(admin.ModelAdmin): 
    list_display = ('student_name', 'course_name', 'approved', 'created_at')

    def student_name(self, obj):
        return obj.get_student_name()

    def course_name(self, obj):
        return obj.get_course_name()

    student_name.short_description = 'Estudiante'
    course_name.short_description = 'Curso'



admin.site.register(Professors)
admin.site.register(Students)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Lessons)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(RelationStudentsCourses, RelationStudentsCoursesAdmin)
admin.site.register(RelationStudentsLessons)