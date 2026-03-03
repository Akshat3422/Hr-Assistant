from rest_framework import serializers
from .models import Recruiter
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recruiter

class CreateRecruiterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    company_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email", "phone", "company_name"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        phone = validated_data.pop("phone")
        company_name = validated_data.pop("company_name")

        user = User.objects.create_user(**validated_data)

        Recruiter.objects.create(
            user=user,
            phone=phone,
            company_name=company_name
        )

        return user


