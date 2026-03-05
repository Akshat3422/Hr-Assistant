from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="recruiter_profile")
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15,blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
