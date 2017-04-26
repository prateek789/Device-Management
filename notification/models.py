from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notification(models.Model):
	module_id=models.CharField(max_length=500)
	message = models.CharField(max_length=500)
	module_name = models.CharField(max_length=100)
	to_user = models.ForeignKey(User,related_name='to_user',default=None,null=True)
	from_user = models.ForeignKey(User,related_name ='from_user',default=None,null=True)
	create_date=models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)
	notification_status = models.BooleanField(default=True)
	class Meta:
		db_table = 'notification'
