from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login


def login(request):
    print('0')
    print(request)
    print('00')
    args = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            args['username'] = username
            login(user)
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