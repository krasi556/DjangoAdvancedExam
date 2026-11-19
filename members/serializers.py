from rest_framework import serializers

from accounts.models import Profile


class RegisterVip(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['is_vip', 'user', 'profile_pic', 'bio', ]

    def create(self, validated_data):
        pass