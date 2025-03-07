from rest_framework import serializers
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from .utils import generate_verification_link


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    avatar = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['uid', 'name', 'last_name', 'phone_number', 'email', 'avatar', 'password']
        read_only_fields = ['uid']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_verified = False  # User must verify email before login
        user.save()

        # ✅ Generate verification link using `reverse()`
        verification_link = f"http://127.0.0.1:8000{generate_verification_link(user)}"

        # ✅ Send email using Brevo
        send_mail(
            subject="Verify your email",
            message=f"Click the link to verify your email: {verification_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return user


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, min_length=1)
#     avatar = serializers.ImageField(required=False, allow_null=True)
#
#     class Meta:
#         model = User
#         fields = ['uid', 'name', 'last_name', 'phone_number', 'email', 'avatar', 'password']
#         read_only_fields = ['uid']
#
#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = User.objects.create(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'phone_number', 'name', 'last_name', 'email', 'avatar']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'avatar']
        read_only_fields = ['phone_number']  # phone_number cannot be updated

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        if 'avatar' in validated_data:
            instance.avatar = validated_data['avatar']

        instance.save()
        return instance





class PasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        fields = ['old_password', 'new_password']

    def validate(self, data):
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError("The new password cannot be the same as the old password.")
        return data



















