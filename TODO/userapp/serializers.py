from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')


class UserCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')