from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer

# Create your views here.
class StudentModelView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseModelView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
