# Generated by Django 4.2.1 on 2023-06-19 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0015_questionlike_object_id_alter_answers_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionlike',
            name='object_id',
        ),
    ]
