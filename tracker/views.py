
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobApplication,Resume
from django.contrib.auth.models import User
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(
                request,
                'registration/register.html',
                {'error': 'Passwords do not match.'}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'registration/register.html',
                {'error': 'Username already exists.'}
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('dashboard')

    return render(request, 'registration/register.html')


@login_required
def job_list(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    jobs = JobApplication.objects.filter(user=request.user)
    if search:
        jobs = jobs.filter(
            company__icontains=search
        )
    if status:
        jobs = jobs.filter(status=status)
    return render(request, 'tracker/job_list.html', {'jobs': jobs})


@login_required
def add_application(request):
    if request.method == 'POST':
        JobApplication.objects.create(
            user=request.user,
            company=request.POST.get('company'),
            role=request.POST.get('role'),
            applied_date=request.POST.get('applied_date'),
            interview_date=request.POST.get('interview_date') or None,
            status=request.POST.get('status'),
            job_url=request.POST.get('job_url'),
            notes=request.POST.get('notes')
        )
        return redirect('job_list')
    return render(request, 'tracker/add_application.html')

@login_required
def edit_application(request, id):
    job = get_object_or_404(
        JobApplication,
        id=id,
        user=request.user
    )
    if request.method == 'POST':
        job.company = request.POST.get('company')
        job.role = request.POST.get('role')
        job.applied_date = request.POST.get('applied_date')
        job.interview_date = request.POST.get('interview_date') or None
        job.status = request.POST.get('status')
        job.job_url = request.POST.get('job_url')
        job.notes = request.POST.get('notes')
        job.save()
        return redirect('job_list')
    return render(request, 'tracker/edit_application.html', {'job': job})

@login_required
def delete_application(request, id):
    job = get_object_or_404(
        JobApplication,
        id=id,
        user=request.user
    )
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')

@login_required
def dashboard(request):

    
    jobs = JobApplication.objects.filter(user=request.user).order_by('-created_at')
    total = jobs.count()
    applied = jobs.filter(status='Applied').count()
    interviews = jobs.filter(status='Interview').count()
    selected = jobs.filter(status='Selected').count()
    rejected = jobs.filter(status='Rejected').count()
    withdrawn = jobs.filter(status='Withdrawn').count()

    context = {
        'total': total,
        'applied': applied,
        'interviews': interviews,
        'selected': selected,
        'rejected': rejected,
        'jobs': jobs,
        'withdrawn':withdrawn,
    }

    return render(request, 'tracker/dashboard.html', context)

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user)

    return render(
        request,
        'tracker/resume_list.html',
        {'resumes': resumes}
    )


@login_required
def add_resume(request):
    if request.method == 'POST':
        is_active = request.POST.get('is_active') == 'on'

        if is_active:
            Resume.objects.filter(user=request.user).update(is_active=False)

        Resume.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            version=request.POST.get('version'),
            file=request.FILES.get('file'),
            is_active=is_active
        )

        return redirect('resume_list')

    return render(request, 'tracker/add_resume.html')

@login_required
def delete_resume(request, id):
    resume = get_object_or_404(
        Resume,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        resume.delete()
        return redirect('resume_list')

@login_required
def set_active_resume(request, id):
    resume = get_object_or_404(
        Resume,
        id=id,
        user=request.user
    )

    Resume.objects.filter(user=request.user).update(is_active=False)

    resume.is_active = True
    resume.save()

    return redirect('resume_list')