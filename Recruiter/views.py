from rest_framework.permissions import BasePermission
from rest_framework import generics
from .serializer import CreateRecruiterSerializer  
from .models import Recruiter


# Only admin can verify the user to post a job 


from rest_framework.permissions import IsAdminUser

class RecruiterCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CreateRecruiterSerializer
    

    
