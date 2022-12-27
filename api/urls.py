from django.urls import path

from . import views

urlpatterns = [
    path('authenticate', views.authenticate, name='authenticate'),
    path('devices', views.devices, name='devices'),
    path('device', views.device, name='device'),
    path('device_reachable', views.device_reachable, name='device_reachable'),
    path('device_toggle', views.device_toggle, name='device_toggle'),
    path('device_on', views.device_on, name='device_on'),
    path('device_off', views.device_off, name='device_off'),
    path('light_temperature', views.light_temperature, name='light_temperature'),
    path('light_color', views.light_color, name='light_color'),
    path('light_brightness', views.light_brightness, name='light_brightness'),
]

