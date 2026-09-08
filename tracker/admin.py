from django.contrib import admin
from .models import JobApplication, Resume


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'status', 'applied_date', 'user')
    list_filter = ('status', 'applied_date')
    search_fields = ('company', 'role')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'user', 'created_at')