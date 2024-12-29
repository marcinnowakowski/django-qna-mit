# Generated by Django 5.1.4 on 2024-12-29 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_remove_question_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveySubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesel', models.CharField(max_length=11)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date submitted')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='qna.question')),
                ('survey_submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qna.surveysubmission')),
            ],
        ),
    ]
