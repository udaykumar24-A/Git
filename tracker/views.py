from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import JobApplicationForm
from .models import JobApplication


@login_required
def dashboard(request):
    applications = JobApplication.objects.filter(user=request.user)

    status_counts = {
        key: applications.filter(status=key).count()
        for key, _ in JobApplication.STATUS_CHOICES
    }

    context = {
        "applications": applications,
        "status_counts": status_counts,
    }
    return render(request, "tracker/dashboard.html", context)


@login_required
def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job_app = form.save(commit=False)
            job_app.user = request.user
            job_app.save()
            return redirect("tracker:dashboard")
    else:
        form = JobApplicationForm()

    return render(request, "tracker/add_application.html", {"form": form})

from django.shortcuts import render

# Create your views here.
