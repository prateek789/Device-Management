from django.shortcuts import render
from django.views.generic import TemplateView
# from blog.models import Blog
from django.core import serializers
# Create your views here.
# class HomePageView(TemplateView):
    
 # def get(self, request, **kwargs):
 #        blog_list = Blog.objects.all().order_by('-publish_date')
 #        context = super(HomePageView, self).get_context_data(**kwargs)
 #        context['blog_list'] = blog_list
 #        return render(request, 'index.html', context)

   # Add this view
# class AboutPageView(TemplateView):
#    template_name = "about.html";
class LoginPageView(TemplateView):
   template_name = "login.html";

def page_not_found(request):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)


def user_error(request):
    return render(request, '500.html', status=500)

def device_error(request):
    return render(request, '500.html', status=500)
    