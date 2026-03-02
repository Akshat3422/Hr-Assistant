from django.urls import path
from .views import RegisterCandidate, ResendOTP, VerifyOTP ,ListCandidates,CandidateProfile,Logout
from rest_framework_simplejwt.views import TokenObtainPairView



urlpatterns = [
    path("register/", RegisterCandidate.as_view(), name="register_candidate"),
    path("verify-otp/", VerifyOTP.as_view(), name="verify_otp"),
    path("resend-otp/", ResendOTP.as_view(), name="resend_otp"),
    path('login/', TokenObtainPairView.as_view(), name='login_candidate'),
    path('logout/',Logout,name="logout"),
    path('',ListCandidates.as_view(), name='list_candidates'),
    path("profile/", CandidateProfile.as_view(), name="candidate_profile"),
]
