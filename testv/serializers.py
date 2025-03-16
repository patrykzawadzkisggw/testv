from rest_framework import serializers
from .models import User, TrustedDevice, UserActivity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'folder']

class TrustedDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustedDevice
        fields = ['id', 'user', 'device_name', 'device_id']

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ['id', 'user', 'login_date', 'service', 'encrypted_login', 'device']
