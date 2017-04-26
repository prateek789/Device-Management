from django.shortcuts import render
from notification.models import Notification
from django.http import HttpResponse
from notification.templatetags import app_filters
from django.db.models import Q
import json
from django.core import serializers
def get_notification(request):
	notification_list = Notification.objects.filter((Q(to_user=request.user) | Q(to_user=None))).exclude((Q(from_user=request.user) | Q(status=0))).order_by('-create_date')[:5]
	if notification_list:
		return render(request,'notification.html',{'notification_list':notification_list})
	else:
		return render(request,'notification.html',{'notification_list':notification_list})
			
    
def read_notification(request):
	noty_id = request.GET['noty_id']
	Notification.objects.filter(id=noty_id).update(status=0)
	data = {'success':'true'}
	return HttpResponse(json.dumps(data), content_type='application/json')

def desktop_notification(request):
	notification_list = Notification.objects.filter(status=1).filter(notification_status=1).order_by('-create_date')[:1]
	data = serializers.serialize("json",notification_list)
	if  notification_list:
		summary ="Request for ownership"
		notify_data = {} 
		notify_data['message'] = notification_list[0].message.capitalize();
		notify_data['subject'] ="Request for ownership"
		data = {'success':'true','notification_data':notify_data}
		Notification.objects.filter(id=notification_list[0].id).update(notification_status=0)
	else:
		data = {'success':'false'}
	return HttpResponse(json.dumps(data), content_type='application/json')




	

