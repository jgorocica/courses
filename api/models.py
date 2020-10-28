from django.db import models
from django.contrib.auth.models import User


class Professors(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return self.user.get_full_name()


class Courses(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título') 
    description = models.TextField(verbose_name='Descripción')
    correlative_id = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Correlativo')
    professor = models.ForeignKey('Professors', on_delete=models.CASCADE, verbose_name='Profesor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Students(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
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
