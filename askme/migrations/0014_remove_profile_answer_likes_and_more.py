# Generated by Django 4.2.1 on 2023-06-19 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0013_answerlike_questionlike_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='answer_likes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='question_likes',
        ),
    ]
