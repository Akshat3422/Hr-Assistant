from rest_framework import serializers
from .models import Candidate

class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(max_length=10)


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)


class ResendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CandidatesList(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)
    id=serializers.StringRelatedField(source="user.id",read_only=True)
    class Meta:
        model=Candidate
        fields=["id","full_name","email","phone"]



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

    