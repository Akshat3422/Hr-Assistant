from django.db import models
from Interview.models import InterviewSession

# Create your models here.
class HRDecision(models.Model):
    interview = models.OneToOneField(InterviewSession, on_delete=models.CASCADE)
    decision = models.CharField(max_length=50, blank=True)  # accepted / rejected / next_round
    notes = models.TextField(null=True, blank=True)
    decided_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"HR Decision for {self.interview.candidate.full_name} - {self.decision}"

