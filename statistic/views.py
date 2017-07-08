from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import datetime

from .models import Day, Article

def days_index(request):
    days = Day.objects.all()   
    days_serialized = serializers.serialize('json', days)
    return JsonResponse(days_serialized, safe=False) 

def days_read(request, timestamp_begin, timestamp_end):
	timestamp_begin_human = datetime.datetime.fromtimestamp(float(timestamp_begin))
	timestamp_end_human = datetime.datetime.fromtimestamp(float(timestamp_end))
	days = Day.objects.filter(created_date__range=(timestamp_begin_human, timestamp_end_human)).order_by('created_date')
	days_serialized = serializers.serialize('json', days)
	return JsonResponse(days_serialized, safe=False) 	

def days_spa(request):
    return render(request, 'statistic/base.html', {})	

def articles_index(request):
    articles = Article.objects.all()   
    articles_serialized = serializers.serialize('json', articles)
    return JsonResponse(articles_serialized, safe=False)     