from django.shortcuts import render,redirect
from category.models import Category,Productlog,OwnershipRequest
from notification.models import Notification
from django.contrib import messages
from category.forms import CategoryForm
from datetime import datetime,timedelta
from dateutil import tz
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.contrib.auth.models import User
from django.db.models import Q
from category.templatetags import product_filters
from django.http import HttpResponse
import json
# Create your views here.


 
def category(request):
	
	if request.user.is_anonymous():
		return redirect("/login")
	owner_list = User.objects.all().exclude(is_superuser=1)
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = Category(
				name = form.cleaned_data['name'],
				description = form.cleaned_data['description'],
				create_date = datetime.now()

				)
			category.created_by = request.user;
			category.save()
			if(category):
				messages.success(request, 'Product added successfully.')
				return redirect("product")
			else:
				messages.warning(request, 'Product could not added.')
				return redirect("product")
		else:
			return render(request, 'product.html', {'form': form,'owner_list':owner_list})
	else:
		return render(request,'product.html',{'form':'','owner_list':owner_list})



def edit_category(request,id):
	if request.user.is_anonymous():
		return redirect("/login")
	# id = request.GET.get('id')	
	category = Category.objects.get(id=id)
	return render(request,'edit.html',{'category':category})

def ownership(request):
	if request.user.is_anonymous():
		return redirect("/login")
	# id = request.GET.get('id')
	category = Category.objects.get(id=request.POST['category_id'])
	if request.method == "POST":
		if  request.POST['owner_id']=='':
			Category.objects.filter(id=request.POST['category_id']).update(owner=request.user,ownership_date=datetime.now())
			log_detail = Productlog.objects.filter(product=request.POST['category_id']).order_by('-current_date')[:1]
			log = Productlog()
			log.user = request.user
			log.product = Category.objects.get(id=request.POST['category_id'])
			if len(log_detail) > 0:
				log.past_user = User.objects.get(id=log_detail[0].user.id)
				log.current_date = log_detail[0].past_date
				Productlog.objects.filter(id=log_detail[0].id).update(past_date=datetime.now(),active=0)    
			log.save()
			text = request.user.username.capitalize()+" take ownership of product "+category.name,
			data = {'messages':text,'title':'Get Ownership'}
			return HttpResponse(json.dumps(data), content_type='application/json')
		else:
			Category.objects.filter(id=request.POST['category_id']).update(owner=None,ownership_date=None)
			OwnershipRequest.objects.filter(product=request.POST['category_id']).update(status=0)
			text = request.user.username.capitalize()+" release ownership of product "+category.name,
			data = {'messages':text,'title':'Release ownership'}
			log_detail = Productlog.objects.filter(product=request.POST['category_id']).order_by('-current_date')[:1]
			log = Productlog()
			log.user = User.objects.get(id=1)
			log.active = 0
			log.product = Category.objects.get(id=request.POST['category_id'])
			if len(log_detail) > 0:
				log.past_user = User.objects.get(id=log_detail[0].user.id)
				log.current_date = log_detail[0].past_date
				Productlog.objects.filter(id=log_detail[0].id).update(past_date=datetime.now(),active=0)    
			log.save()
			return HttpResponse(json.dumps(data), content_type='application/json')
			

def request_to_ownership(request):
	if request.method == "POST":
		# print(request.POST['category_id']);
		to_user = User.objects.get(id=request.POST['owner_id'])
		category_detail = Category.objects.get(id=request.POST['category_id'])
		# print(category_detail)
		request_ownership = OwnershipRequest()
		request_ownership.product = Category.objects.get(id=request.POST['category_id'])
		request_ownership.user = request.user
		request_ownership.save();
		notification = Notification(
			module_id = request.POST['category_id'],
			message = request.user.username+" send request to change ownership for product "+category_detail.name,
			module_name = 'Category'
			)
		notification.to_user = to_user
		notification.from_user = request.user
		notification.save()
		if(notification.id>0):
			messages.success(request,'Change Ownership request send successfully.')
			return redirect("product")
		else:
			messages.warning(request, 'Your are not able to send Change Ownership request.')
			return redirect("product")

def change_ownership(request,id):
	if request.user.is_anonymous():
		return redirect("/login")
	# id = request.GET.get('id')
	#noty = Notification.objects.get(id=id)
	category = Category.objects.get(id=id)
	owner_list = OwnershipRequest.objects.filter(Q(product = id) & Q(status = 1)) 
	if request.method == "POST":
		if  request.POST['ownership']=="1":
			try:
				owner_id = request.POST['owner']
				owner_obj = User.objects.get(username=owner_id)
				Category.objects.filter(id=id).update(owner=owner_obj,ownership_date=datetime.now())
				OwnershipRequest.objects.filter(product=id).filter(user_id=owner_obj).update(status=0)
				log_detail = Productlog.objects.filter(product=id).order_by('-current_date')[:1]
				log = Productlog()
				log.user = owner_obj
				log.product = Category.objects.get(id=id)
				if len(log_detail) > 0:
					log.past_user = User.objects.get(id=log_detail[0].user.id)
					log.current_date = log_detail[0].past_date
					Productlog.objects.filter(id=log_detail[0].id).update(past_date=datetime.now(),active=0)  
				log.save()
				messages.success(request, 'Ownership change successfully.')
			except  User.DoesNotExist:
				messages.warning(request, 'Ownership could not change successfully.')
			return redirect("product")
		else:
			messages.warning(request, 'Ownership not change.')
			return redirect("product")
				
	else:
		return render(request,'change_to_ownership.html',{'category':category,'owner_list':owner_list})     	    	

def product_log(request,id):
	if request.user.is_anonymous():
		return redirect("/login")
	log_list = Productlog.objects.filter(product=id).order_by('-current_date')
	product_detail = Category.objects.get(id=id)
	paginator = Paginator(log_list,10)
	page = request.GET.get('page')
	try:
		logs = paginator.page(page)
	except PageNotAnInteger:
		logs = paginator.page(1)
	except EmptyPage:
		logs = paginator.page(paginator.num_pages)
	
	return render(request,'product_log.html',{'form':'','logs':logs,'product_detail':product_detail})


def get_table(request):
	product_name = request.GET.get('product_name')
	product_owner = request.GET.get('product_owner')
	ownership_date = request.GET.get('ownership_date')
	if ownership_date:
		ownership_date.strip()
		dates = ownership_date.strip().split('/')
		start_date = dates[0].strip()
		start_date = datetime.strptime(start_date, "%Y-%m-%d")
		end_date = dates[1].strip()
		end_date = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)
		
	category_list = Category.objects.all()
	if product_name:
		category_list = category_list.filter(name__icontains=product_name).order_by('-ownership_date')
	
	if product_owner:
		category_list = category_list.filter(owner=product_owner).order_by('-ownership_date')
	
	if ownership_date:
	 	category_list = category_list.filter(ownership_date__range = [start_date,end_date]).order_by('-ownership_date')
    
	#category_list = category_list.order_by('-id')
	
	paginator = Paginator(category_list,5)
	page = request.GET.get('page')
	try:
		categories = paginator.page(page)
	except PageNotAnInteger:
		categories = paginator.page(1)
	except EmptyPage:
		categories = paginator.page(paginator.num_pages)
	return render(request,'category.html',{'form':'','categories':categories})

def convertTimeZone(date):
	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('Asia/Kolkata')
	utc = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
	utc = utc.replace(tzinfo=from_zone)
	central = utc.astimezone(to_zone)
	return central.strftime('%Y-%m-%d %H:%M:%S')
 
