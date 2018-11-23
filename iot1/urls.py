from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^traffic$', views.traffic, name='traffic'),
    url(r'^overspeed$', views.overspeed, name='overspeed'),
    #url(r'^driverregister/$', views.DriverRegister, name='DriverRegister'),
]
