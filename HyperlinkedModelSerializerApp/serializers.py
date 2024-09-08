from dataclasses import field
from rest_framework import serializers
from rest_framework_nested import serializers as sl
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework.reverse import reverse
from .models import Student, Course, Diploma

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
class CourseSerializer(sl.NestedHyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'rating', 'student']


class DiplomaSerializer(sl.NestedHyperlinkedModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Diploma
        fields = ['url', 'student', 'rating']

    def get_url(self, obj):
            # Dynamically build the URL using the reverse function and the student's primary key
            request = self.context.get('request')
            return reverse(
                'student-diplomas-detail',
                kwargs={
                    'student_pk': obj.student.pk,
                    'pk': obj.pk
                },
                request=request
            )

class StudentSerializer(sl.NestedHyperlinkedModelSerializer):
    diplomas = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='student-diplomas-detail',
        parent_lookup_kwargs={'student_pk': 'student__pk'}
    )
    
    # The detailed content diplomas
    # diploma_details = DiplomaSerializer(source='diploma_set', many=True, read_only=True)  # Change 'a' to 'diploma_details' for clarity

    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'roll', 'city', 'diplomas']

