from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=100)
	description=models.CharField(max_length=500)
	create_date=models.DateTimeField()
	created_by = models.ForeignKey(User)
	owner = models.ForeignKey(User,related_name ='owner',default=None,null=True,blank=True)
	ownership_date = models.DateTimeField(default=None,null=True,blank=True)
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'category'
		verbose_name = 'Product'
		verbose_name_plural = 'Products'


class Productlog(models.Model):
	product=models.ForeignKey(Category)
	user= models.ForeignKey(User,related_name ='current_user')
	past_user= models.ForeignKey(User,related_name ='past_user',default=None,null=True)
	current_date = models.DateTimeField(auto_now_add=True)
	past_date = models.DateTimeField(default=None,null=True)
	create_date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	class Meta:
		db_table = 'product_log'

class OwnershipRequest(models.Model):
	product=models.ForeignKey(Category,related_name ='requested_product')
	user= models.ForeignKey(User,related_name ='requested_user')
	status = models.BooleanField(default=True)
	create_date = models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'ownership_request'		