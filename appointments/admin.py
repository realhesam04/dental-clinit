from django.contrib import admin

from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'doctor',
        'service',
        'date',
        'status',
        'start_time',
        'end_time',
    ]

    list_filter = (
        'doctor',
        'date',
        'status',
        'service',
    )

    search_fields = (
        'patient__user__first_name',
        'patient__user__last_name',
        'patient__user__phone',
        'doctor__user__first_name',
        'doctor__user__last_name',
        'service__name',
    )

    ordering = (
        '-date',
        '-start_time'
    )

    list_editable = (
        'status',
    )

    list_per_page = 25
