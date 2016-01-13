import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from vehicle import urls as vehicle_urls
from rent import urls as rent_urls
from account import urls as account_urls

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'rent.views.home', name='home'),
    url(r'^', include(vehicle_urls)),
    url(r'^', include(account_urls)),
    url(r'^', include(rent_urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),   
    url(r'^admin/', include(admin.site.urls))   
) 

if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
