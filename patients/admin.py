from django.contrib import admin

from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'get_full_name',
        'gender',
        'date_of_birth',
        'created_at',
    ]
    list_filter = (
        'gender',
    )
    search_fields = (
        'user__firstname',
        'user__lastname',
        'user__username',
        'user__phone',
    )
    ordering = (
        '-created_at',
    )

    @admin.display(description='Patient')
    def get_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.username

    