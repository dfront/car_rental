from django.conf.urls import url
from rent import views

urlpatterns = [
    url(r'^rents/$', views.rent_list),
    url(r'^makeRent/$', views.rent_create),
]
