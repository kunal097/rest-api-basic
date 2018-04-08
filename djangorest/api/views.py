from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics , mixins , status , request
from .models import User
from .serializers import UserListSerializer , UserUpdateSerializer







class UserRudView(generics.ListAPIView):
    # lookup_field = ''
    serializer_class = UserListSerializer


    def get_queryset(self):
        return User.objects.all()


class UserAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = UserUpdateSerializer


    def get_queryset(self):
        return User.objects.all()


