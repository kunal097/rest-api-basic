from rest_framework import serializers

from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'user_id',
            'name',
            'address',
            'gender',


        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'user_id',
            'name',
            'address',

            'gender',


        ]

        read_only_fields = [
            'name',
            'address',
            ]
