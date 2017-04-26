from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^login', views.user_login,name='login'),
    url(r'^logout', views.user_logout,name='logout'),
]