from django.urls import path
from rest_framework.routers import DefaultRouter

from members.views import EmployeeViewSet

router = DefaultRouter()

router.register('members',EmployeeViewSet, basename='members')

urlpatterns = router.urls
