from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializers,UserCustomSerializers



class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UserCustomSerializers
        return UserSerializers