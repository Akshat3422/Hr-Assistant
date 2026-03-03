from django.urls import path
from .views import RecruiterCreate

urlpatterns=[
    path('create/',RecruiterCreate.as_view(),name="recruiter_create")
]