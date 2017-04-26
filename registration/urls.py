from django.conf.urls import url
from registration import views

urlpatterns = [
    url(r'^registration',views.registration,name='registration'),
   # url(r'^registration/add$', views.create, name='add'),	
]