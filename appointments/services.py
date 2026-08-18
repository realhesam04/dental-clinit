from datetime import datetime, timedelta

from doctors.models import Availability
from .models import Appointment


def get_available_slots(doctor, service, date):
    """
    Return available start times for a doctor, service and date.
    """

    weekday = date.weekday()

    availability = Availability.objects.filter(
        doctor=doctor,
        weekday=weekday,
        is_active=True,
    ).first()

    if not availability:
        return []

    appointments = Appointment.objects.filter(
        doctor=doctor,
        date=date,
        status__in=[
            Appointment.Status.PENDING,
            Appointment.Status.CONFIRMED,
        ],
    )

    slots = []

    current_time = datetime.combine(
        date,
        availability.start_time,
    )

    end_datetime = datetime.combine(
        date,
        availability.end_time,
    )

    duration = timedelta(
        minutes=service.duration,
    )

    while current_time + duration <= end_datetime:

        slot_start = current_time.time()
        slot_end = (current_time + duration).time()

        is_available = True

        for appointment in appointments:

            if (
                slot_start < appointment.end_time
                and slot_end > appointment.start_time
            ):
                is_available = False
                break

        if is_available:
            slots.append(slot_start)

        current_time += duration

    return slots

