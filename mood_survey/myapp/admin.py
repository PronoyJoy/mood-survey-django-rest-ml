from django.contrib import admin
from . models import MentalHealthEntry
# Register your models here.

@admin.register(MentalHealthEntry)
class MentalHealthEntryAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'mood',
        'anxiety_level',
        'stress_level',
        'energy_level',
        'focus_level',
        'medication_taken',
        'created_at',
    )

    list_filter = (
        'mood',
        'medication_taken',
        'date',
    )

     # Add a search box that queries these text fields
    search_fields = (
        'notes',
        'medication_notes',
    )

    # Make these timestamp fields read-only (you won’t accidentally edit them)
    readonly_fields = (
        'date', 'created_at', 'updated_at'
    )

    fieldsets = (
         (None, {
            'fields': ('date', 'mood'),
        }),

        ('Levels (1–10)', {
            'fields': (
                'anxiety_level',
                'stress_level',
                'energy_level',
                'focus_level',
            )
        }),

         ('Notes & Medication', {
            'fields': ('notes', 'medication_taken', 'medication_notes')
        }),

         ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # collapsible section
        }),
    )
