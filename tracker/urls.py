from django.urls import path
from . import views
from .api import JobApplicationListCreateAPIView, JobApplicationDetailAPIView


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('applications/', views.job_list, name='job_list'),
    path('add/', views.add_application, name='add_application'),
    path('resumes/', views.resume_list, name='resume_list'),
    path('resumes/add/', views.add_resume, name='add_resume'),
    path('resumes/set-active/<int:id>/', views.set_active_resume, name='set_active_resume'),
    path('resumes/delete/<int:id>/', views.delete_resume, name='delete_resume'),
    path('edit/<int:id>/', views.edit_application, name='edit_application'),
    path('delete/<int:id>/', views.delete_application, name='delete_application'),

    path('api/jobs/', JobApplicationListCreateAPIView.as_view(), name='api_job_list_create'),
    path('api/jobs/<int:pk>/', JobApplicationDetailAPIView.as_view(), name='api_job_detail'),
]