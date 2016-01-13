from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^login/$', views.LoginView),
    url(r'^api/auth/$', views.AuthView.as_view(), name='authenticate')
]
