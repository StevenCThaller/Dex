from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register$', views.register),
    url(r'^adduser$', views.add_user),
    url(r'^login$', views.login)
]