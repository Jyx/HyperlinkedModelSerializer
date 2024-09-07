from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi/',views.StudentModelView, basename='student')
router.register('course/',views.CourseModelView, basename='course')

urlpatterns = [
    path('',include(router.urls)),
]
