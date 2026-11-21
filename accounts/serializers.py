from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import Profile

ModelUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUser
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['created_at', 'user', ]
