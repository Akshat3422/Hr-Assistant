from django.urls import path
from .views import CandidateListCreateView, CandidateDetailView

urlpatterns = [
    path("", CandidateListCreateView.as_view(), name="candidate_list_create"),
    path("<str:pk>/", CandidateDetailView.as_view(), name="candidate_detail"),
]