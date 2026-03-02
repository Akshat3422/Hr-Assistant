from rest_framework import serializers
from .models import Candidate

class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(max_length=10)


class OTPVerificationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    otp = serializers.CharField(max_length=6)


class ResendOTPSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)


class CandidatesList(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)
    username=serializers.CharField(source="user.username",read_only=True)
    id=serializers.StringRelatedField(source="user.id",read_only=True)
    class Meta:
        model=Candidate
        fields=["id","full_name","email","phone","username"]



class CandidateUpdate(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", required=False)

    class Meta:
        model = Candidate
        fields = ["full_name", "phone", "email"]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})

        # update candidate fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # update user email
        if "email" in user_data:
            instance.user.email = user_data["email"]
            instance.user.save()

        return instance

    