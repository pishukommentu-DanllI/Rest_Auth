from rest_framework import serializers
from .models import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Subject


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student

    def to_representation(self, instance):
        representation = super(StudentSerializer, self).to_representation(instance)
        representation['subject'] = SubjectSerializer(instance.subject, many=False).data
        return representation


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Class

    def to_representation(self, instance):
        representation = super(ClassSerializer, self).to_representation(instance)
        representation['students'] = StudentSerializer(instance.students, many=True).data
        return representation
