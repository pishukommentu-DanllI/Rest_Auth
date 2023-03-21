from django.contrib import admin
from .models import *


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'age', 'subject', 'mark')
    list_editable = ('fio', 'age', 'subject', 'mark')
    list_filter = ('fio', 'age', 'subject', 'mark')
    search_fields = ('fio', 'age', 'subject', 'mark')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    list_editable = ('name', 'year')
    list_filter = ('name', 'year')
