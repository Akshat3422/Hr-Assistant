from django.urls import path
from .views import RegisterCandidate, ResendOTP, VerifyOTP 



urlpatterns = [
    path("register/", RegisterCandidate.as_view(), name="register_candidate"),
    path("verify-otp/", VerifyOTP.as_view(), name="verify_otp"),
    path("resend-otp/", ResendOTP.as_view(), name="resend_otp"),
]
