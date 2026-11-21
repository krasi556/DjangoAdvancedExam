from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from accounts.models import Profile
from accounts.serializers import UserSerializer
from employees.models import Employee

UserModel = get_user_model()


class RegisterVip(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['is_vip', 'user', 'profile_pic', 'bio', ]


class UserWriteSerialize(serializers.ModelSerializer):

    def validate(self, attrs):
        user_id = self.parent.initial_data['user'].get('id')

        if user_id is not None:
            try:
                attrs['user_instance'] = UserModel.objects.get(pk=user_id)
            except UserModel.DoesNotExist:
                raise ValidationError("doesnt exist")

        user_serializer = UserSerializer(data=attrs)
        user_serializer.is_valid(raise_exception=True)
        attrs['user_data'] = user_serializer.validated_data
        return attrs





    class Meta:
        model = UserModel
        fields = '__all__'



class EmployeeWriteSerialize(serializers.ModelSerializer):
    user = UserWriteSerialize()

    class Meta:
        model = Employee
        fields = '__all__'
