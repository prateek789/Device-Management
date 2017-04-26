"""demo_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (
   handler404, handler500
)
handler404 = 'myapp.views.page_not_found'
handler500 = 'myapp.views.server_error'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('myapp.urls')),
    url(r'^', include('login.urls')),
    url(r'^', include('registration.urls')),
    # url(r'^', include('blog.urls')),
    url(r'^', include('category.urls')),
    # url(r'^', include('comment.urls')),
    url(r'^', include('notification.urls')),
    # url(r'^', include('api.urls')),
    url(r'^', include('password_reset.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
