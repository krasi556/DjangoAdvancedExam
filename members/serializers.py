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
        find_user_id = self.parent.initial_data.get('user', {})
        user_id = find_user_id.get('id')
        if user_id is not None:
            try:
                user_id = int(user_id)
            except (ValueError, TypeError):
                raise ValidationError({'user':'must be a number'})
            try:
                attrs['user_instance'] = UserModel.objects.get(pk=user_id)
            except UserModel.DoesNotExist:
                raise ValidationError("doesnt exist")
        elif not attrs.get('password'):
            raise ValidationError({'password': 'Password is required when creating a new user.'})
        return attrs

    def create(self, validated_data):
        user = validated_data.pop('user_instance', None)
        if user is None:
            password = validated_data.pop('password', None)
            user = UserModel(**validated_data)
            user.set_password(password)
            user.save()
        return user

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'email': {'required': False},
            'username': {'required': False},
            'password': {'required': False, 'write_only': True}
        }


class EmployeeWriteSerialize(serializers.ModelSerializer):
    user = UserWriteSerialize(required=False, allow_null=True)

    class Meta:
        model = Employee
        fields = '__all__'
