# Generated by Django 4.2.1 on 2023-06-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0010_remove_profile_answer_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='answer_likes',
            field=models.ManyToManyField(to='askme.answers'),
        ),
    ]
