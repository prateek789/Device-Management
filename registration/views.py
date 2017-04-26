from django.shortcuts import render,redirect
from registration.forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages

# def registration(request):
# 	 return render(request, 'registration.html')

def registration(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
        	user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
            )
       		if(user):
        		messages.success(request, 'User add successfully.')
       			return redirect("login")
        	else:
        		messages.error(request, 'User could not added.')
        		return redirect("registration")
        else:
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request, 'registration.html', {'form': ''})

