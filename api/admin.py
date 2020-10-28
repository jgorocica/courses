# Admin tools
from django.contrib import admin

# Models 
from .models import (Professors, Students, Courses,
                    Lessons, Questions, Answers)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'professor', 'created_at')


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'created_at')
    

class AnswersAdmin(admin.ModelAdmin):
    list_display = ('title', 'question', 'question_lesson' , 'is_correct', 'created_at')

    def question_lesson(self, obj):
        return obj.question.lesson.title


admin.site.register(Professors)
admin.site.register(Students)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Lessons)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers, AnswersAdmin)