from django.urls import path

from .views import UploadResume,ListCandidateResume,ResumeProfile

# Upload Resume and Job Rolees
# List all resumes and job roles of all candidates

urlpatterns=[
    path('upload-resume/', UploadResume.as_view(), name='upload_resume'),
    path('',ListCandidateResume.as_view(),name="my_resumes"),
    path('<str:pk>',ResumeProfile.as_view(),name="resume_detail")
]