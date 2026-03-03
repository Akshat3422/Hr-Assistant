from django.db import models

# Create your models here.
class JobRole(models.Model):
    title = models.CharField(max_length=255)
    required_skills = models.JSONField()
    experience_required = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title