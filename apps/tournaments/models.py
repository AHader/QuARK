from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from apps.teams.models import Team
from sorl.thumbnail import ImageField

User = get_user_model()


class Tournament(models.Model):
    date = models.DateTimeField()
    name = models.CharField(
        max_length=100,
    )
    image = ImageField(_("Team Logo"), upload_to="team_logos", blank=True)

    def __str__(self):
        return self.name


class Roster(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='rosters')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tournaments')
    players = models.ManyToManyField(User, related_name='tournaments')

    def __str__(self):
        return "{} - {}".format(self.team.name, self.players.count())
