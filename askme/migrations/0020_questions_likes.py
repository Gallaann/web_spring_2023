# Generated by Django 4.2.1 on 2023-06-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0019_answers_answer_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
