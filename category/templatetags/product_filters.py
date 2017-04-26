from django import template
from notification.models import Notification
from category.models import OwnershipRequest,Category
from django.db.models import Q
import timeago,datetime
from dateutil import tz
register = template.Library()

@register.filter(name='check_make_request')
def check_make_request(value,request):
	results =  OwnershipRequest.objects.filter((Q(product=value) & Q(status=1))).order_by('create_date')
	if(len(results)>0):
		dict = []
		i = 0; 
		for ownership_user in results:
			if ownership_user.user == request.user:
				user = 'You'
			else:
				user = ownership_user.user.username.capitalize()
			   	
			dict.insert(i,user)
			i = i+1
		return dict;	
	else:
		return None

@register.filter(name='check_request_btn')
def check_request_btn(value,request):
	results =  OwnershipRequest.objects.filter((Q(status=1) & Q(product=value) & Q(user=request.user)))
	return len(results);

@register.filter(name='change_owner_check')
def change_owner_check(value,request):
	check_owner = Category.objects.filter((Q(id=value) & Q(owner=request.user)))
	check_request=OwnershipRequest.objects.filter((Q(status=1) & Q(product=value)))
	if check_owner and check_request:
		return 1;	

@register.filter(name='duration_date_string')
def duration_date_string(date1,date2):
	if date2==None:
		format_date = timeago.format(date1.strftime("%Y-%m-%d %H:%M:%S"),datetime.datetime.now())
	else:
		format_date = timeago.format(date1.strftime("%Y-%m-%d %H:%M:%S"),date2.strftime("%Y-%m-%d %H:%M:%S"))
	return format_date.replace('ago','')


@register.filter(name='convertTimeZone')
def convertTimeZone(date):
	date = date.strftime("%Y-%m-%d %H:%M:%S")
	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('Asia/Kolkata')
	utc = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
	utc = utc.replace(tzinfo=from_zone)
	central = utc.astimezone(to_zone)
	return central.strftime('%B %d, %Y %I:%M %p')		
