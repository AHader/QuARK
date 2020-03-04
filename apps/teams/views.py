from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.edit import FormView

from .models import Team, Transfer, Role
from .forms import JoinForm, TransferForm


class TeamListing(ListView):
    model = Team


class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'ngb', 'image']
    success_url = '/'

    def form_valid(self, form):
        #Staff.objects.new(role="Founder", player=self.request.user, team=self.instance)
        return super(TeamCreate, self).form_valid(form)


class TeamDetail(DetailView):
    model = Team


class TeamUpdate(UpdateView):
    model = Team

    fields = ['name', 'ngb', 'image']

    def get_success_url(self):
        return reverse('team:detail', kwargs={
            'pk': self.object.pk,
        })


class TeamDelete(DeleteView):
    model = Team
    success_url = '/'


class TransferCreate(CreateView):
    model = Transfer
    success_url = '/'

    def get_form_class(self):
        if self.request.user.is_new:
            return JoinForm
        else:
            return TransferForm

    def form_valid(self, form):
        form.instance.to_team = Team.objects.get(pk=self.kwargs['pk'])
        form.instance.player = self.request.user
        if self.request.user.is_new:
            # TODO: To make our life easy we automatically accept
            form.instance.state = 'a'
        return super(TransferCreate, self).form_valid(form)
