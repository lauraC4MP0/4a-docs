from django.db.models import query
from models.users import User
from rest_framework import generics
#from serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    #serializer_class=UserSerializer