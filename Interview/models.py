from django.db import models
from candidate.models import Candidate
from JobRole.models import JobRole   

# Create your models here.
class InterviewSession(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Interview for {self.candidate.full_name} - {self.job_role.title}"



class InterviewQuestion(models.Model):
    interview = models.ForeignKey(InterviewSession, on_delete=models.CASCADE)
    question_text = models.TextField()
    category = models.CharField(max_length=100)  # knowledge, behaviour etc
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Question for {self.interview.candidate.full_name} - {self.category}"



class InterviewResponse(models.Model):
    question = models.ForeignKey(InterviewQuestion, on_delete=models.CASCADE)
    answer_text = models.TextField()
    transcript = models.TextField(null=True, blank=True)
    confidence_score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Response for {self.question.interview.candidate.full_name} - {self.question.category}"




class InterviewScore(models.Model):

    interview = models.OneToOneField(
        InterviewSession,
        on_delete=models.CASCADE,
        related_name="score"
    )

    knowledge_score = models.FloatField()
    experience_score = models.FloatField()
    communication_score = models.FloatField()
    team_skill_score = models.FloatField()
    behavioural_score = models.FloatField()

    total_score = models.FloatField(editable=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        self.total_score = (
            self.knowledge_score +
            self.experience_score +
            self.communication_score +
            self.team_skill_score +
            self.behavioural_score
        )
        super().save(*args, **kwargs)