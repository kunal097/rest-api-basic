from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserListSerializer , UserUpdateSerializer


# Create your views here.

class UserAPIView(generics.CreateAPIView):
    # lookup_field = 'user_id'
    serializer_class  = UserUpdateSerializer


    def get_queryset(self):
        return User.objects.all()

    def perform_create(self , serializer):

        serializer.save()



class UserRudView(generics.ListAPIView):
    # lookup_field = ''
    serializer_class = UserListSerializer


    def get_queryset(self):
        return User.objects.all()
