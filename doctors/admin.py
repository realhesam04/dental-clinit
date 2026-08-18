from django.contrib import admin

from .models import Doctor, Availability


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'get_full_name',
        'specialty',
        'experience',
        'is_active',
        'created_at',
    )

    list_filter = (
        'specialty',
        'is_active',
    )

    search_fields = (
        'user__first_name',
        'user__last_name',
        'user__username',
        'user__phone',

    )
    ordering = ('-created_at',)

    @admin.display(description='Doctor')
    def get_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
    

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        'doctor',
        'weekday',
        'start_time',
        'end_time',
        'is_active',
    )

    list_filter = (
        'weekday',
        'is_active',
        'doctor',
    )

    ordering = (
        'doctor',
        'weekday',
        'start_time',
    )
    