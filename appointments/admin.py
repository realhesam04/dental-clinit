from django.contrib import admin, messages

from .models import Appointment
from .services import get_available_slots


@admin.action(description='Show available time slots')
def show_available_slots(modeladmin, request, queryset):
    for appointment in queryset:
        slots = get_available_slots(
            doctor=appointment.doctor,
            service=appointment.service,
            date=appointment.date,
        )

        if slots:
            formatted_slots = ', '.join(
                slot.strftime('%H:%M')
                for slot in slots
            )

            modeladmin.message_user(
                request,
                f'{appointment.doctor} | '
                f'{appointment.date} | '
                f'{appointment.service}: '
                f'{formatted_slots}',
                messages.SUCCESS,
            )
        else:
            modeladmin.message_user(
                request,
                f'No available slots for '
                f'{appointment.doctor} on {appointment.date}.',
                messages.WARNING,
            )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'doctor',
        'service',
        'date',
        'start_time',
        'end_time',
        'status',
    )

    list_editable = (
        'status',
    )

    list_filter = (
        'status',
        'date',
        'doctor',
        'service',
    )

    search_fields = (
        'patient__user__first_name',
        'patient__user__last_name',
        'patient__user__phone',
        'doctor__user__first_name',
        'doctor__user__last_name',
        'doctor__user__phone',
        'service__name',
    )

    ordering = (
        '-date',
        '-start_time',
    )

    list_per_page = 25

    actions = (
        show_available_slots,
    )