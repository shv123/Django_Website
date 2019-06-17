from rest_framework import serializers
from django.contrib.auth.models import User

class DriveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
#       fields = '__all__'
        fields = (
            'username',
            'email',
            'password',
            'url'
        )