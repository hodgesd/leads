from django.db import models

# Create your models here.
from django.db import models

class Lead(models.Model):
    address = models.CharField(max_length=255, verbose_name="Address")
    phone = models.CharField(max_length=15, verbose_name="Phone")
    email = models.EmailField(verbose_name="Email")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.address} - {self.email}"