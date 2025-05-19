from django.db import models

class MentalHealthEntry(models.Model):
    # When this entry was logged
    date = models.DateField(auto_now_add=True)

    MOOD_CHOICES = [
        ('very_happy', 'Very Happy'),
        ('happy',      'Happy'),
        ('neutral',    'Neutral'),
        ('sad',        'Sad'),
        ('anxious',    'Anxious'),
        ('stressed',   'Stressed'),
    ]
    mood = models.CharField(max_length=12, choices=MOOD_CHOICES)

    anxiety_level = models.PositiveSmallIntegerField(
        default=1,
        help_text="1 (low) to 10 (high)"
    )
    stress_level  = models.PositiveSmallIntegerField(
        default=1,
        help_text="1 (low) to 10 (high)"
    )
    energy_level  = models.PositiveSmallIntegerField(
        default=5,
        help_text="1 (exhausted) to 10 (energized)"
    )
    focus_level   = models.PositiveSmallIntegerField(
        default=5,
        help_text="1 (distracted) to 10 (laser focus)"
    )

    notes = models.TextField(blank=True)

    medication_taken = models.BooleanField(default=False)
    medication_notes = models.TextField(
        blank=True,
        help_text="Dosage, time, effect notes…"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Mental health entries"

    def __str__(self):
        return f"{self.date} – mood:{self.mood}"
