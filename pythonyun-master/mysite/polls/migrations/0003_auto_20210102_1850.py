# Generated by Django 3.1.2 on 2021-01-02 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_homework_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Homework',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]