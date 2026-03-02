import random
import os
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

def generate_otp():
    """Generates a 6-digit OTP."""
    return random.randint(100000, 999999)



def send_otp_email(user):
    """Sends an OTP email to the user."""
    subject = "Your OTP for HR Assistant"
    otp=generate_otp()
    user.otp=otp
    user.otp_created_at=timezone.now()
    user.save()
    message = f"Hello {user.full_name},\n\nYour OTP is: {user.otp}\n\nThis OTP is valid for 10 minutes."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list,fail_silently=False)