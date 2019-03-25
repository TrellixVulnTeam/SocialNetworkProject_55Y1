from django.conf import settings
from django.conf.urls import url
from .views import DetailViewT, ListViewT, CreateViewT, UpdateViewT, DeleteViewT
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^(?P<pk>\d+)/delete/$', DeleteViewT.as_view(), name='delete'),
    url(r'^(?P<pk>\d*)/$', DetailViewT.as_view(),name='detail'),
    url(r'^(?P<pk>\d*)/update/$', UpdateViewT.as_view(), name='update'),
    url(r'^search/', ListViewT.as_view(), name='list'),
    url(r'^create/$', CreateViewT.as_view(), name='create'),
    url(r'^$', RedirectView.as_view(url="/")),
]

