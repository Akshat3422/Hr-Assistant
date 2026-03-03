from rest_framework.serializers import ModelSerializer
from .models import Resume
from rest_framework import serializers
from candidate.models import Candidate


class ResumeUpload(ModelSerializer):
    class Meta:
        model=Resume
        fields=["file"]


class ResumeListSerializer(ModelSerializer):
    candidate_name = serializers.CharField(source="candidate.user.username")
    candidate_phone_number=serializers.CharField(source="candidate.phone")

    class Meta:
        model = Resume
        fields = ["id", "file", "candidate_name","candidate_phone_number","is_processed"]


class ResumeSerializer(ModelSerializer):
    candidate_name = serializers.CharField(source="candidate.user.username")
    candidate_phone_number=serializers.CharField(source="candidate.phone")

    class Meta:
        model = Resume
        fields = ["id", "file", "candidate_name","candidate_phone_number","extracted_skills","is_processed"]