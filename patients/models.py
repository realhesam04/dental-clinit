from django.db import models
from django.conf import settings

class Patient(models.Model):
    GENDER_CHOICE = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_profile',
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICE,
        blank=True,
    )
    address = models.TextField(
        blank=True,
    )
    medical_notes = models.TextField(
        blank=True,
        help_text= "General mdeical notes",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

