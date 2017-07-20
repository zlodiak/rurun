from django.shortcuts import render
from django.utils import timezone

from .models import Message


def message_create(request):
		m = Message(name='qwe', text='fgfjgj', published_date=timezone.now(), created_date=timezone.now());
		m.save();
