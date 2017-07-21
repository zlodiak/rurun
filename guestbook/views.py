from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
import json

from .models import Message


def message_create(request):
		if (len(request.POST['message']) > 200) or (len(request.POST['name']) > 60):
			status = '0'
			error_message = 'Хакир штоль?'
		else:
			status = '1'
			error_message = ''
			m = Message(name=request.POST['name'], text=request.POST['message'], published_date=timezone.now(), created_date=timezone.now(),)
			m.save();

		data = json.dumps({ 'status': status , 'error_message': error_message })

		return JsonResponse(data, safe=False)     		
