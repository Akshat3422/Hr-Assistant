from .serializer import JobDescription,JobList
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import JobRole

class IsVerifiedRecruiter(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, "recruiter_profile") and
            request.user.recruiter_profile.is_verified
        )
    



class RegisterJob(APIView):
    permission_classes = [IsVerifiedRecruiter]   # custom permission

    def post(self, request):
        serializer = JobDescription(data=request.data)

        if serializer.is_valid():
            serializer.save(recruiter=request.user.recruiter_profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class ListJobs(generics.ListAPIView):
    # ek Recruiter ki sari jobs posted
    permission_classes=[IsVerifiedRecruiter]
    serializer_class=JobList
    def get_queryset(self):
        return JobRole.objects.filter(recruiter=self.request.user.recruiter_profile) #type:ignore
    
    

class ModifyJobs(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsVerifiedRecruiter]
    serializer_class=JobDescription
    def get_queryset(self):
        return JobRole.objects.filter(recruiter=self.request.user.recruiter_profile) #type:ignore
    


