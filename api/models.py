# Models
from django.db import models
from django.contrib.auth.models import User

# Choices
from .choices import TYPE_QUESTIONS_CHOICES

class Professors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return self.user.get_full_name()


class Courses(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título') 
    description = models.TextField(verbose_name='Descripción')
    correlative_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Correlativo')
    professor = models.ForeignKey('Professors', on_delete=models.CASCADE, verbose_name='Profesor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.title


class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    courses = models.ManyToManyField('Courses', through="RelationStudentsCourses", related_name='students')

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.user.get_full_name()


class RelationStudentsCourses(models.Model):
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, verbose_name='Curso')
    student = models.ForeignKey('Students', on_delete=models.CASCADE, verbose_name='Estudiante')
    approved = models.BooleanField(default=False, verbose_name='Aprobado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Relación Estudiante-Curso'
        verbose_name_plural = 'Relación Estudiantes-Cursos'

    def get_student_name(self):
        return '%s %s' % (self.student.user.first_name, self.student.user.last_name)

    def get_course_name(self):
        return '%s' % (self.course.title)


class Lessons(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título') 
    correlative = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Correlativo')
    is_mandatory = models.BooleanField(default=False, verbose_name='Obligatorio')
    approval_score = models.FloatField(null=True, blank=True, verbose_name='Puntaje de aprobación')
    courses = models.ForeignKey('Courses', on_delete=models.CASCADE, related_name='lessons')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Lección'
        verbose_name_plural = 'Lecciones'

    def __str__(self):
        return self.title


class Questions(models.Model): 
    title = models.CharField(max_length=100, verbose_name='Pregunta') 
    score = models.FloatField(default=1.0, verbose_name='Puntaje')
    lesson = models.ForeignKey('Lessons', on_delete=models.CASCADE, verbose_name='Lección')
    question_type = models.IntegerField(choices=TYPE_QUESTIONS_CHOICES, verbose_name='Tipo de pregunta')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.title


class RelationStudentsLessons(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE, verbose_name='Estudiante')
    lesson = models.ForeignKey('Lessons', on_delete=models.CASCADE, verbose_name='Lección')
    assigned_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de asignación')
    approved = models.BooleanField(default=False, verbose_name='Aprobado')
    student_score = models.FloatField(default=0.0, verbose_name='Puntaje obtenido')


class Answers(models.Model):
    question = models.ForeignKey('Questions', on_delete=models.CASCADE, blank=False, null=True, verbose_name='Pregunta')
    title = models.CharField(max_length=100, verbose_name='Respuesta')
    is_correct = models.BooleanField(default=False, verbose_name='¿Esta respuesta es correcta?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return self.title

    def get_question_title(self):
        return '%s' % self.question.title