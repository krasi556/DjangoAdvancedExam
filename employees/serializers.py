from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from rest_framework import serializers

from accounts.models import User
from accounts.serializers import  ProfileSerializer
from employees.models import Employee

UserModel = get_user_model()

class EmployeeSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # profession = serializers.CharField(max_length=20)
    # years_of_experience = serializers.IntegerField(
    #     validators=[MaxValueValidator(50),
    #                 ]
    # )
    user = ProfileSerializer(read_only=True)

    # user_ = serializers.PrimaryKeyRelatedField(
    #     queryset=UserModel.objects.all(),
    #     source='user',
    #     write_only=True
    # )

    class Meta:
        model = Employee
        fields = '__all__'
