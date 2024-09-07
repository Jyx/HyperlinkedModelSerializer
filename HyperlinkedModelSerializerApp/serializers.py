from dataclasses import field
from rest_framework import serializers
from rest_framework_nested import serializers as sl
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from .models import Student, Course, Diploma

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
class CourseSerializer(sl.NestedHyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','rating']


class DiplomaSerializer(sl.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'student_pk' : 'student__pk',
    }
    class Meta:
        model = Diploma
        fields = '__all__'

DEBUG=0
# class StudentSerializer(serializers.HyperlinkedModelSerializer):
class StudentSerializer(sl.NestedHyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id','url','name','roll','city', 'diplomas']
        # fields = ['id','url','name','roll','city']

    diplomas = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,   # Or add a queryset
        view_name='student-diplomas-detail',
        parent_lookup_kwargs={'student_pk': 'student__pk'}
                            # ^-- Nameserver queryset will .filter(domain__pk=domain_pk)
                            #     being domain_pk (ONE underscore) value from URL kwargs
        )
