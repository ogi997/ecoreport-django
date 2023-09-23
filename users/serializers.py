from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "password"]

    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        print(validate_data)
        user = User.objects.create(**validate_data)
        user.save()
        return user


class UserIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'date_joined', 'is_superuser', 'is_admin', 'is_staff',
            'is_active', 'is_superuser'
        )
        read_only_fields = (
            'first_name', 'last_name', 'email', 'date_joined', 'is_superuser', 'is_admin', 'is_staff',
            'is_active', 'is_superuser'
        )


class ChangeUserDataSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        read_only_fields = ("first_name", "last_name", "email")

    def update(self, instance, validate_data):
        instance.first_name = validate_data['first_name']
        instance.last_name = validate_data['last_name']
        instance.email = validate_data['email']
        instance.save()
        print("vraca instance")
        return instance


class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True, required=True)
    password_old = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("password", "password_repeat", "password_old")

    def validate_old_password(self, value):
        user = self.context['request'].user
        err_msg = "Wrong old password"
        print(value)
        if not user.check_password(value):
            raise serializers.ValidationError(err_msg)
        return True

    def validate(self, data):
        err_msg1 = "Password didn't match"
        err_msg2 = "Please enter different new password."
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError(err_msg1)
        elif data['password'] == data['password_old']:
            raise serializers.ValidationError(err_msg2)
        else:
            if self.validate_old_password(data['password_old']):
                return data

    def update(self, instance, validated_data):
        print(validated_data)
        instance.password = make_password(validated_data['password'])
        instance.save()

        return instance
