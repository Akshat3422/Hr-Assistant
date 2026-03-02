from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


phone_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message="Enter a valid 10-digit Indian phone number starting with 6-9."
)

password_validator = RegexValidator(
    regex=r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
    message="Password must be at least 8 characters long and include at least one letter, one number, and one special character."
)

# Create your models here.
class Candidate(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='candidate_profile'
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, validators=[phone_validator], unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



