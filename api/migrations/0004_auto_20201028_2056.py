# Generated by Django 3.1.2 on 2020-10-29 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201028_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api.questions', verbose_name='Pregunta'),
        ),
        migrations.DeleteModel(
            name='RelationQuestionsAnswers',
        ),
    ]
