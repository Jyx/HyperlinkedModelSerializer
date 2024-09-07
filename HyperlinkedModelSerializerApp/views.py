from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Course, Diploma
from .serializers import StudentSerializer, CourseSerializer, DiplomaSerializer

# Create your views here.
class StudentModelView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseModelView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DiplomaModelView(viewsets.ModelViewSet):
    serializer_class = DiplomaSerializer

    def get_queryset(self):
        return Diploma.objects.filter(student=self.kwargs['student_pk'])
