from dataclasses import field
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Student, Course, Diploma

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'rating', 'student']


class DiplomaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Diploma
        fields = ['url', 'student', 'rating']

    def get_url(self, obj):
            request = self.context.get('request')
            return reverse(
                'student-diplomas-detail',
                kwargs={
                    'student_pk': obj.student.pk,
                    'pk': obj.pk
                },
                request=request
            )

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    diplomas = DiplomaSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='student-detail')
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'roll', 'city', 'diplomas']

