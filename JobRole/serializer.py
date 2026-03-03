from rest_framework import  serializers
from .models import JobRole


class JobDescription(serializers.ModelSerializer):
    class Meta:
        model=JobRole
        fields= "__all__"



class JobList(serializers.ModelSerializer):
    recruiter_name=serializers.CharField(source="Recruiter.user.username")
    class Meta:
        model=JobRole
        fields=["title","recruiter_name","required_skills"]