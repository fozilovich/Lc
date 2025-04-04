# Generated by Django 5.1.7 on 2025-03-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses_app', '0001_initial'),
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(related_name='student_groups', to='users_app.student'),
        ),
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ManyToManyField(related_name='teaching_groups', to='users_app.teacher'),
        ),
    ]
