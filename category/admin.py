from category.models import Category
from django.contrib import admin
from django.apps import AppConfig

class CategoryAdmin(admin.ModelAdmin):
	list_display    = ['name', 'description','create_date','owner']
    
admin.site.register(Category, CategoryAdmin)
