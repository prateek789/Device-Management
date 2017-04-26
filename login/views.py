from django.shortcuts import render,redirect
from login.forms import LoginForm
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
# Create your views here.
def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.warning(request,'Invalid credential')
				return redirect('/login')
		else:
			return render(request, 'login.html', {'form': form})
	else:
		 return render(request, 'login.html',{'form':''})
	
def user_logout(request):
    logout(request)
    messages.success(request,'User logout successfully')
    return redirect('/login')


