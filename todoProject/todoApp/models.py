from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

def validate_no_past_date(value):
    if value < timezone.now().date():
        raise ValidationError('Deadline cannot be in the past.')

class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = 'H', 'High'
        MEDIUM = 'M', 'Medium'
        LOW = 'L', 'Low'
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=1,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    deadline = models.DateField(
        validators=[validate_no_past_date],
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        deadline_str = f" - Due: {self.deadline}" if self.deadline else ""
        return f"{self.title} ({self.get_priority_display()}){deadline_str}"