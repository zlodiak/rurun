from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
# from django.core.context_processors import csrf
# from django.views.decorators.csrf import csrf
# from django.views.decorators.csrf import csrf_protect
# from django.template.context_processors import csrf

def login(request):
    args = {}
    if request.POST:
    		print(1)
    		username = request.POST.get('username', '')
    		password = request.POST.get('password', '')
    		user = auth.authenticate(username=username, password=password)
    		if user is not None:
    				auth.login(request, user)
    				return redirect('/')
    		else:
    				args['login_error'] = 'Пользователь не найден';
    				return render(request, 'login.html', args)
    else:
    		print(2)
    		return render(request, 'login.html', args)


def logout(request):    		
		auth.logout(request)
		return redirect('/')