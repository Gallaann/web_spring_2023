# Generated by Django 4.2.1 on 2023-06-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0006_like_remove_questions_likes_count_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AlterField(
            model_name='questions',
            name='likes',
            field=models.ManyToManyField(to='askme.profile'),
        ),
    ]