from django.conf.urls import url
from category import views

urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^$',views.category,name='product'),
    url(r'^edit_category/(?P<id>[0-9]+)/$',views.edit_category,name='edit_category'),
    url(r'^ownership',views.ownership,name='ownership'),
    url(r'^request_to_ownership',views.request_to_ownership,name='request_to_ownership'),
    url(r'^change-ownership/(?P<id>[0-9]+)/$',views.change_ownership,name='change-ownership'),
    url(r'^owner-details/(?P<id>[0-9]+)/$',views.product_log,name='owner-details'),
    url(r'^get-table',views.get_table,name='get-table'),
]