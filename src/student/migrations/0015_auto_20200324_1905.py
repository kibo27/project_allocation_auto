# Generated by Django 3.0.4 on 2020-03-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_student_regno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='regno',
            field=models.IntegerField(),
        ),
    ]