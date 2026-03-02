from django.db import models

from candidate.models import Candidate

# Create your models here.
class Resume(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE,related_name="resumes")
    file = models.FileField(upload_to="resumes/")
    parsed_data = models.JSONField(null=True, blank=True)
    extracted_text = models.TextField(null=True, blank=True)
    resume_score=models.FloatField(null=True, blank=True)
    is_processed = models.BooleanField(default=False)
    extracted_skills = models.JSONField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Resume of {self.candidate.full_name}"




class JobRole(models.Model):
    title = models.CharField(max_length=255)
    required_skills = models.JSONField()
    experience_required = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title