from dataclasses import field
from rest_framework import serializers
from .models import Student, Course


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id','url','name','roll','city']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','rating']


