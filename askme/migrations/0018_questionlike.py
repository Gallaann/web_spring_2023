# Generated by Django 4.2.1 on 2023-06-19 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0017_delete_questionlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='askme.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='askme.profile')),
            ],
        ),
    ]