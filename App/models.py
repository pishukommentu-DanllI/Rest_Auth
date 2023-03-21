from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name='Предмет')

    def __str__(self):
        return self.name


class Student(models.Model):
    CHOICE_MODELS = (
        ('1', '2'),
        ('2', '3'),
        ('3', '4'),
        ('4', '5'),
    )
    fio = models.CharField(max_length=255, verbose_name='Фамилия Имя Отчество')
    age = models.IntegerField(verbose_name='Возраст')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    mark = models.CharField(choices=CHOICE_MODELS, default=4, max_length=9)

    def __str__(self):
        return self.fio


class Class(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    year = models.IntegerField(verbose_name='Год обучения')
    students = models.ManyToManyField(Student, verbose_name='Студенты')

    def __str__(self):
        return self.name
