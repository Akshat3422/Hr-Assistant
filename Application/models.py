from django.db import models

class Application(models.Model):

    candidate = models.ForeignKey(
        'candidate.Candidate',
        on_delete=models.CASCADE,
        related_name='applications'
    )

    job_role = models.ForeignKey(
        'Resume.JobRole',
        on_delete=models.CASCADE,
        related_name='applications'
    )

    resume = models.ForeignKey(
        'Resume.Resume',
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=30,
        default="APPLIED"
    )

    application_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate', 'job_role')

    def __str__(self):
        return f"{self.candidate} - {self.job_role}"