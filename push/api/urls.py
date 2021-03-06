from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from devices.views import DeviceViewSet
from tokens.views import TokenViewSet
from messages.views import MessagesViewSet
from accounts.views import AccountViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(prefix=r'devices', viewset=DeviceViewSet, base_name='device')
router.register(prefix=r'tokens', viewset=TokenViewSet, base_name='token')
router.register(prefix=r'messages', viewset=MessagesViewSet, base_name='message')
router.register(prefix=r'accounts', viewset=AccountViewSet, base_name='account')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
