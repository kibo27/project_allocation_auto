# Generated by Django 3.0.4 on 2020-03-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20200323_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='regno',
            field=models.IntegerField(default=2, editable=False),
            preserve_default=False,
        ),
    ]
