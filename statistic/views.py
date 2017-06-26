from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import datetime

from .models import Day

def days_index(request):
    days = Day.objects.all()   
    days_serialized = serializers.serialize('json', days)
    return JsonResponse(days_serialized, safe=False) 

def days_read(request, timestamp_begin, timestamp_end):
	print('===========')
	# 10 June 2017 г., 14:17:40
	# 1497104260
	# 20 June 2017 г., 14:17:40
	# 1497968260
	# http://127.0.0.1:8000/days/1497104260/1497968260/
	timestamp_begin_human = datetime.datetime.fromtimestamp(float(timestamp_begin))
	timestamp_end_human = datetime.datetime.fromtimestamp(float(timestamp_end))
	print('------------')
	print(timestamp_begin_human)
	days = Day.objects.filter(created_date__range=(timestamp_begin_human, timestamp_end_human)).order_by('created_date')
	days_serialized = serializers.serialize('json', days)
	return JsonResponse(days_serialized, safe=False) 	

def days_spa(request):
    return render(request, 'statistic/base.html', {})	