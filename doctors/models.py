from django.conf import settings
from django.db import models

class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile',
    )

    specialty = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    image = models.ImageField(
        upload_to='doctors/',
        blank=True,
        null=True,
    )

    experience = models.PositiveIntegerField(
        default=0,
        help_text='Years of professional experience',
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.specialty}"
