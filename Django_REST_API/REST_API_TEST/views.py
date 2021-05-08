from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from REST_API_TEST.serializes import UserSerializer, GroupSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [Permission.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [Permission.IsAuthenticated]

