from django.db import models




TYPES = (
        ('Gas Leak', 'Gas Leak'),
        ('Meter Reading', 'Meter Reading'),
        ('Connection Setup', 'Connection Setup'),
    )

class ServiceRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPES)
    details = models.TextField()
    attached_file = models.FileField(upload_to='attachments/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.customer_name} - {self.type}"