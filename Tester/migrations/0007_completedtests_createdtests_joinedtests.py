# Generated by Django 3.2 on 2021-06-05 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tester', '0006_rename_test_access_code_test_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinedTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tester.test')),
                ('userEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tester.user')),
            ],
        ),
        migrations.CreateModel(
            name='CreatedTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tester.test')),
                ('userEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tester.user')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tester.test')),
                ('userEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tester.user')),
            ],
        ),
    ]