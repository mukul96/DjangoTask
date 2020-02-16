from rest_framework.serializers import ModelSerializer
from .models import  UserInfo

class UserSerializer(ModelSerializer):
    class Meta:
        model=UserInfo
        fields='__all__'
