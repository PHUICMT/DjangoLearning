from django.contrib.auth.models import User, Group
from rest_framework import serializes

class UserSerializer(serializes.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializes.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']