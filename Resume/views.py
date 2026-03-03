from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Resume
from .serializers import ResumeUpload,ResumeListSerializer,ResumeSerializer
from .tasks import process_resume

from candidate.models import Candidate

class UploadResume(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        if 'file' not in request.FILES:
            return Response(
                {"error": "No file provided"},
                status=400
            )

        serializer = ResumeUpload(data=request.data)

        if serializer.is_valid():

            try:
                candidate = Candidate.objects.get(user=request.user)
            except Candidate.DoesNotExist:
                return Response(
                    {"error": "Candidate profile not found"},
                    status=400
                )

            serializer.save(candidate=candidate)
            resume = serializer.instance
            process_resume.delay(resume.id) #type:ignore

            return Response(
                {"message": "Resume uploaded successfully"},
                status=201
            )

        return Response(serializer.errors, status=400)



class ListCandidateResume(generics.ListAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ResumeListSerializer
    def get_queryset(self):
        return Resume.objects.filter(
            candidate=self.request.user.candidate_profile #type:ignore
        )
   




class ResumeProfile(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeSerializer

    def get_object(self):
        return get_object_or_404(
            Resume,
            id=self.kwargs["pk"],
            candidate__user=self.request.user
        )
    
