from django.db import models

class Lead(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="new", choices=[
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("closed", "Closed"),
    ])

    def __str__(self):
        return f"{self.email} - {self.status}"