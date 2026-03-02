from django.urls import path
from .views import RegisterCandidate, ResendOTP, VerifyOTP ,LoginCandidate



urlpatterns = [
    path("register/", RegisterCandidate.as_view(), name="register_candidate"),
    path("verify-otp/", VerifyOTP.as_view(), name="verify_otp"),
    path("resend-otp/", ResendOTP.as_view(), name="resend_otp"),
    path('login/', LoginCandidate.as_view(), name='login_candidate'),
    # path('',ListCandidates.as_view(), name='list_candidates'),
    # path('<int:pk>/', CandidateDetail.as_view(), name='candidate_detail'),
]
