from django.contrib import admin
from .models import Student, Course

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']

admin.site.register(Course)
