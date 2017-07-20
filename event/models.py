from django.db import models
from django.utils import timezone


class Date(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title     

class Event(models.Model):
		date = models.ForeignKey(Date, on_delete=models.CASCADE)
		day = models.CharField(max_length=20, default='0')
		title = models.CharField(max_length=200)
		text = models.TextField()
		order = models.IntegerField(default=0)
		created_date = models.DateTimeField(default=timezone.now)
		published_date = models.DateTimeField(blank=True, null=True)

		def __str__(self):
		    return self.title             