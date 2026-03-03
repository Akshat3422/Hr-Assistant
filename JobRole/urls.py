from django.urls import path
from . import views


urlpatterns=[
    path('register/',views.RegisterJob.as_view(),name="job_post"),
    path('',views.ListJobs.as_view(),name="List_all_job_posted_by_a_recruiter"),
    path('<str:pk>/',views.ModifyJobs.as_view(),name="modify_jobs")
]