# Generated by Django 3.2 on 2021-06-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tester', '0002_test_totalmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='totalMarks',
            field=models.IntegerField(default=0),
        ),
    ]
