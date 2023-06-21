# Generated by Django 4.2.1 on 2023-05-21 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0002_answers_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='question',
        ),
        migrations.AddField(
            model_name='questions',
            name='tags',
            field=models.ManyToManyField(to='askme.tags'),
        ),
    ]