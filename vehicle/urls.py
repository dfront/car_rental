from django.conf.urls import url
from vehicle import views

urlpatterns = [
    url(r'^vehicles/$', views.vehicle_list),
    url(r'^vehicle/(?P<pk>[0-9]+)/$', views.vehicle_detail),
]
