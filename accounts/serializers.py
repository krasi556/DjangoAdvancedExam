from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password as django_validate_password
from accounts.models import Profile

ModelUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    def validate_password(self,value):
        pass
    class Meta:
        model = ModelUser
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['created_at', 'user', ]
