from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Tournament, Roster


class TournamentListing(ListView):
    model = Tournament


class TournamentCreate(CreateView):
    model = Tournament
    fields = ['name', 'date', 'image']
    success_url = '/'


class TournamentDetail(DetailView):
    model = Tournament


class TournamentUpdate(UpdateView):
    model = Tournament

    fields = ['name', 'date', 'image']

    def get_success_url(self):
        return reverse('tournament:detail', kwargs={
            'pk': self.object.pk,
        })


class TournamentDelete(DeleteView):
    model = Tournament
    success_url = '/'


class RosterCreate(CreateView):
    model = Roster
    success_url = '/'
    fields = ['players']

    def form_valid(self, form):
        form.instance.tournament = Tournament.objects.get(pk=self.kwargs['pk'])
        form.instance.team = self.request.user.team
        return super(RosterCreate, self).form_valid(form)
