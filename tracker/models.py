from django.conf import settings
from django.db import models


class JobApplication(models.Model):
    STATUS_APPLIED = "applied"
    STATUS_INTERVIEW = "interview"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_APPLIED, "Applied"),
        (STATUS_INTERVIEW, "Interview"),
        (STATUS_REJECTED, "Rejected"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_applications",
    )
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_APPLIED,
    )
    applied_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-applied_date", "-id"]

    def __str__(self) -> str:
        return f"{self.company_name} - {self.position or 'N/A'} ({self.get_status_display()})"
