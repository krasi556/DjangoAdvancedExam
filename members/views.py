from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from employees.models import Employee
from members.permissions import EmployeeTierAccess
from members.serializers import EmployeeWriteSerialize, CasualEmployee


# Create your views here.


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, EmployeeTierAccess]
    queryset = Employee.objects.all()
    serializer_class = EmployeeWriteSerialize # THIS WILL BE CHANGED  WITH EmployeeWriteSerialize IF I GOT TIME LEFT !!!!!!
