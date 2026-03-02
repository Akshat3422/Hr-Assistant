from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message="Enter a valid 10-digit Indian phone number starting with 6-9."
)

# Create your models here.
class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,validators=[phone_validator], unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



