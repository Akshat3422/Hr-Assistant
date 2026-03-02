import random
import os
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

def generate_otp():
    """Generates a 6-digit OTP."""
    return random.randint(100000, 999999)



def send_otp_email(candidate):
    """Sends an OTP email to the user."""
    subject = "Your OTP for HR Assistant"
    otp=generate_otp()
    candidate.otp=otp
    candidate.otp_created_at=timezone.now()
    candidate.save()
    message = f"Hello {candidate.full_name},\n\nYour OTP is: {candidate.otp}\n\nThis OTP is valid for 10 minutes."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [candidate.user.email]
    send_mail(subject, message, from_email, recipient_list,fail_silently=False)