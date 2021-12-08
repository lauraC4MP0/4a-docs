from rest_framework import serializers
from authApp.models.users import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','username','password','name','lastname','email']