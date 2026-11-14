from django.core.validators import MaxValueValidator
from rest_framework import serializers

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # profession = serializers.CharField(max_length=20)
    # years_of_experience = serializers.IntegerField(
    #     validators=[MaxValueValidator(50),
    #                 ]
    # )
    class Meta:
        model = Employee
        fields = '__all__'
