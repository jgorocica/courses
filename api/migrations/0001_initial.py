# Generated by Django 3.1.2 on 2020-10-28 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('correlative_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.courses', verbose_name='Correlativo')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('is_mandatory', models.BooleanField(default=False, verbose_name='Obligatorio')),
                ('approval_score', models.FloatField(blank=True, null=True, verbose_name='Puntaje de aprobación')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('correlative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lessons', verbose_name='Correlativo')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='api.courses')),
            ],
            options={
                'verbose_name': 'Lección',
                'verbose_name_plural': 'Lecciones',
            },
        ),
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.CreateModel(
            name='RelationStudentsCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False, verbose_name='Aprobado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.courses', verbose_name='Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('courses', models.ManyToManyField(related_name='students', through='api.RelationStudentsCourses', to='api.Courses')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='RelationStudentsLessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de asignación')),
                ('approved', models.BooleanField(default=False, verbose_name='Aprobado')),
                ('student_score', models.FloatField(default=0.0, verbose_name='Puntaje obtenido')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lessons', verbose_name='Lección')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.students', verbose_name='Estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='relationstudentscourses',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.students', verbose_name='Estudiante'),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Pregunta')),
                ('score', models.FloatField(default=1.0, verbose_name='Puntaje')),
                ('question_type', models.IntegerField(choices=[(0, 'BOOLEAN'), (1, 'MULTIPLE CHOICE, ONE ANSWER CORRECT'), (2, 'MULTIPLE CHOICE, MORE THAN ONE ANSWER IS CORRECT'), (3, 'MULTIPLE CHOICE, MORE THAN ONE ANSWER IS CORRECT, ALL MUST BE ANSWERED CORRECTLY')], verbose_name='Tipo de pregunta')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lessons', verbose_name='Lección')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.professors', verbose_name='Profesor'),
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Respuesta')),
                ('is_correct', models.BooleanField(default=False, verbose_name='¿Esta respuesta es correcta?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questions', verbose_name='Pregunta')),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
            },
        ),
    ]
