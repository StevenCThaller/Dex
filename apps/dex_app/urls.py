from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.versionselect),
    # url(r'^fighting$', views.setFighting),
    url(r'^moves/(?P<gen>[a-zA-Z0-9 -]+)$', views.moves),
    url(r'^moveshow/(?P<gen>[a-zA-Z0-9 -]+)/(?P<move>[a-zA-Z0-9 -]+)$', views.moveshow),
    url(r'^(?P<gen>[a-on-xzA-ON-XZ0-9 -]+)$', views.pokedex),
    url(r'^(?P<gen>[a-on-xzA-ON-XZ0-9 -]+)/(?P<id>\d+)$', views.dex_page),
    url(r'^types$', views.types),
    url(r'^types/(?P<type>\w+)$', views.showtypes)
]