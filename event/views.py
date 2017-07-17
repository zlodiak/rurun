from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import datetime

from .models import Date, Event

def events_index(request):
    events = Event.objects.all()   
    events_serialized = serializers.serialize('json', events)
    return JsonResponse(events_serialized, safe=False) 

def dates_index(request):
    dates = Date.objects.all()   
    dates_serialized = serializers.serialize('json', dates)
    return JsonResponse(dates_serialized, safe=False)     
