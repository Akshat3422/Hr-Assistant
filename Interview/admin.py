from django.contrib import admin
from .models import InterviewQuestion,InterviewResponse,InterviewScore,InterviewSession

# Register your models here.

admin.site.register(InterviewQuestion)
admin.site.register(InterviewResponse)
admin.site.register(InterviewScore)
admin.site.register(InterviewSession)

