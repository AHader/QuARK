from django.conf.urls import url

from .views import TeamCreate, TeamDelete, TeamDetail, TeamListing, TeamUpdate, TransferCreate


app_name = 'teams'

urlpatterns = [
    url(r'^$', TeamListing.as_view(), name='list'),
    url(r'^create/$', TeamCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TeamDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TeamUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TeamDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/transfer/$', TransferCreate.as_view(), name='transfer'),
]


