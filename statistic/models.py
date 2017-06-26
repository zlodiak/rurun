from django.db import models
from django.utils import timezone

class Day(models.Model):
    author = models.ForeignKey('auth.User')
    pulse_avg_bpm = models.IntegerField()
    pulse_max_bpm = models.IntegerField()
    training_time_min = models.IntegerField()
    desc = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.created_date.strftime('%Y-%m-%d %H:%M')