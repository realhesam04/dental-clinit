from django.db import models
from django.urls import reverse

class Service(models.Model):
    name = models.CharField(max_length=150)

    slug = models.SlugField(
        max_length=150,
        unique=True,
        )
    
    description = models.TextField()

    duration = models.PositiveIntegerField(
        help_text= "Duration in minutes",
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
    
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            'services:detail',
            kwargs={'slug': self.slug}
        )
    