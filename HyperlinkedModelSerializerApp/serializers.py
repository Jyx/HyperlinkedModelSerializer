from dataclasses import field
from rest_framework import serializers
from rest_framework_nested import serializers as sl
from .models import Student, Course, Diploma



# class CourseSerializer(serializers.HyperlinkedModelSerializer):
class CourseSerializer(sl.NestedHyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','rating']


class DiplomaSerializer(sl.NestedHyperlinkedModelSerializer):
    class Meta:
        model = Diploma
        fields = '__all__'

DEBUG=0
# class StudentSerializer(serializers.HyperlinkedModelSerializer):
class StudentSerializer(sl.NestedHyperlinkedModelSerializer):
    if DEBUG:
        print("Running diploma serializers")
        diploma = serializers.HyperlinkedRelatedField(
                many=True,
                read_only=True,
                view_name='student-diplomas-list'
                )
        class Meta:
            model = Student
            fields = ['id','url','name','roll','city', 'diploma']
    else:
        diplomas = DiplomaSerializer(many=True, read_only=True)
        class Meta:
            model = Student
            fields = ['id','url','name','roll','city', 'diplomas']
