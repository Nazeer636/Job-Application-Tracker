from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    applied_date = models.DateField()
    interview_date = models.DateField(blank=True, null=True)
    status = models.CharField(
    max_length=20,
    choices=[
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        ('Withdrawn', 'Withdrawn'),
    ],
    default='Applied'
)
    job_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    file = models.FileField(upload_to='resumes/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)