# Generated by Django 4.1.2 on 2023-03-21 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Предмет')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='Фамилия Имя Отчество')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('mark', models.CharField(choices=[(1, 2), (2, 3), (3, 4), (4, 5)], default=4, max_length=5)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.subject', verbose_name='Предмет')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('year', models.IntegerField(verbose_name='Год обучения')),
                ('students', models.ManyToManyField(to='App.student', verbose_name='Студенты')),
            ],
        ),
    ]