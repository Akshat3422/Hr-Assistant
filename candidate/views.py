from datetime import timedelta
from django.utils import timezone
from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .utils import send_otp_email
from django.contrib.auth import authenticate
from .models import Candidate
import re
from .serializers import  OTPVerificationSerializer, RegisterSerializer, ResendOTPSerializer,LoginSerializer


class RegisterCandidate(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data

        email = data.get("email")
        password = data.get("password")
        full_name = data.get("full_name")
        phone = data.get("phone")

        if not email or not password:
            return Response(
                {"error": "Email and password required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if  not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password):
            return Response(
                {"error": "Password must be at least 8 characters long and include at least one letter, one number, and one special character."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check existing user
        if User.objects.filter(username=email).exists():
            return Response(
                {"error": "Email already registered"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create user (password automatically hashed)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        existing_candidate = Candidate.objects.filter(phone=phone, is_verified=False).first()

        if existing_candidate:
            existing_candidate.user.delete()

        # Create candidate profile
        candidate = Candidate.objects.create(
            user=user,
            full_name=full_name,
            phone=phone,
            is_verified=False
        )

        send_otp_email(candidate)
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
            candidate = Candidate.objects.get(user__email=email)
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
            candidate = Candidate.objects.get(user__email=email)
            send_otp_email(candidate)
            return Response({"message": "OTP resent to email"})
        except Candidate.DoesNotExist:
            return Response({"message": "Candidate not found"}, status=404)
        




class LoginCandidate(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"message": "Email and password required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=email, password=password)

        if not user:
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            candidate = Candidate.objects.get(user__email=email)
        except Candidate.DoesNotExist:
            return Response(
                {"message": "Candidate profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if not candidate.is_verified:
            return Response(
                {"message": "Candidate not verified"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"message": "Login successful"},
            status=status.HTTP_200_OK
        )