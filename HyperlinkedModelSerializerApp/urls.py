from django.contrib.admin.utils import lookup_field
from django.urls import path,include
from pprint import pprint
from rest_framework_nested import routers

# from HyperlinkedModelSerializerApp.models import Student
app_name = 'studentapis'

from .import views

router = routers.DefaultRouter()
router.register(r'studentapis', views.StudentModelView)
router.register(r'courses', views.CourseModelView)

diploma_router = routers.NestedSimpleRouter(router, r'studentapis', lookup='studentapi')
diploma_router.register(r'diplomas', views.DiplomaModelView, basename='student-diplomas')

urlpatterns = router.urls + diploma_router.urls
pprint(urlpatterns)
