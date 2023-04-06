from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.postobjects.all()
    serializer_class = UserSerializer
    pass

class UserDetail(generics.RetrieveDestroyAPIView):
    pass 