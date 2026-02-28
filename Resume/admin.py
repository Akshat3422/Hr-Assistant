from django.contrib import admin

from .models import JobRole, Resume

# Register your models here.
admin.site.register(Resume)
admin.site.register(JobRole)