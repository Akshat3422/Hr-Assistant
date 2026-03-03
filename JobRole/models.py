from django.db import models
from Recruiter.models import Recruiter

# Create your models here.
class JobRole(models.Model):
    recruiter = models.ForeignKey(
        'Recruiter.Recruiter',   # app_name.ModelName
        on_delete=models.CASCADE,
        related_name='job_roles'  ,
        null=True,
    blank=True # important for reverse relation
    )
    title = models.CharField(max_length=255)
    required_skills = models.JSONField(null=True,blank=True)
    experience_required = models.FloatField()
    full_text=models.CharField(max_length=1000,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title