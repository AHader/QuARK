from django.conf.urls import url

from .views import TournamentCreate, TournamentDelete, TournamentDetail, TournamentListing, TournamentUpdate, RosterCreate


app_name = 'tournament'

urlpatterns = [
    url(r'^$', TournamentListing.as_view(), name='list'),
    url(r'^create/$', TournamentCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TournamentDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TournamentUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TournamentDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/roster/$', RosterCreate.as_view(), name='roster'),
]


