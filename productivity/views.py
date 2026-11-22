from django.shortcuts import render, redirect
from .models import Task


def dashboard(request):
    if request.method == "POST":
        Task.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            priority=request.POST.get("priority"),
            due_date=request.POST.get("due_date"),
            reminder_time=request.POST.get("reminder_time") or None,
        )
        return redirect("dashboard")

    tasks = Task.objects.all().order_by("due_date")

    context = {
        "tasks": tasks,
        "total_tasks": tasks.count(),
        "pending_tasks": tasks.filter(status="Pending").count(),
        "completed_tasks": tasks.filter(status="Completed").count(),
    }

    return render(request, "productivity/dashboard.html", context)
