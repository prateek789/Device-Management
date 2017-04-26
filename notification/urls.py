from django.conf.urls import url
from notification import views

urlpatterns = [

     url(r'^get-notification',views.get_notification,name='get-notification'),
     url(r'^desktop-notification',views.desktop_notification,name='desktop-notification'),
     url(r'^read-notification',views.read_notification,name='read-notification'),
     
]