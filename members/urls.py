from django.urls import path
from rest_framework.routers import DefaultRouter

from members.views import EmployeeViewSet

router = DefaultRouter()

router.register('employees',EmployeeViewSet.as_view(), basename='employees')

urlpatterns = router.urls
