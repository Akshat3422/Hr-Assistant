from datetime import timedelta
from django.utils import timezone
from django.db import transaction
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .utils import send_otp_email
from .models import Candidate
from .serializers import CandidateSerializer, OTPVerificationSerializer, ResendOTPSerializer

class RegisterCandidate(generics.CreateAPIView):
    serializer_class = CandidateSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        candidate = serializer.save(is_verified=False)
        send_otp_email(candidate)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "OTP sent to email"},
            status=status.HTTP_201_CREATED
        )


class VerifyOTP(generics.GenericAPIView):
    serializer_class = OTPVerificationSerializer

    def post(self,request):
        email = request.data.get("email")
        otp = request.data.get("otp")
        try:
            candidate = Candidate.objects.get(email=email)
            if not candidate.otp or not candidate.otp_created_at:
                return Response({"message": "OTP not generated"}, status=400)
            
            if candidate.otp == otp  and timezone.now()- candidate.otp_created_at < timedelta(minutes=2): 
                candidate.is_verified = True
                candidate.otp = None
                candidate.otp_created_at = None
                candidate.save(update_fields=["is_verified", "otp", "otp_created_at"])
                return Response({"message": "Candidate verified successfully"})
            else:
                return Response({"message": "Invalid OTP or OTP expired"}, status=400)
        except Candidate.DoesNotExist:
            return Response({"message": "Candidate not found"}, status=404)
        

class ResendOTP(generics.GenericAPIView):
    serializer_class = ResendOTPSerializer

    def post(self,request):
        email = request.data.get("email")
        try:
            candidate = Candidate.objects.get(email=email)
            send_otp_email(candidate)
            return Response({"message": "OTP resent to email"})
        except Candidate.DoesNotExist:
            return Response({"message": "Candidate not found"}, status=404)