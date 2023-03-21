from .serializer import *
from .premissions import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class SubjectApi:
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (SubjectPermission,)


class SubjectListView(SubjectApi, ListCreateAPIView):
    """Класс API для предметов ListCreate"""


class SubjectRetrieveUpdateDestroyAPIView(SubjectApi, RetrieveUpdateDestroyAPIView):
    """Класс API для предметов RetrieveUpdate"""


class StudentApi:
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (StudentPermission,)


class StudentListView(StudentApi, ListCreateAPIView):
    """Класс API для Учеников ListCreate"""


class StudentRetrieveUpdateDestroyAPIView(StudentApi, RetrieveUpdateDestroyAPIView):
    """Класс API для Учеников RetrieveUpdate"""


class ClassApi:
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (ClassPermission,)


class ClassListView(ClassApi, ListCreateAPIView):
    """Класс API для классов ListCreate"""


class ClassRetrieveUpdateDestroyAPIView(ClassApi, RetrieveUpdateDestroyAPIView):
    """Класс API для классов RetrieveUpdate"""
