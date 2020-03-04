from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from multiselectfield import MultiSelectField
from sorl.thumbnail import ImageField

User = get_user_model()

NGB_CHOICES =(
    ("AQArg","Argentina"),
    ("QA","Australia"),
    ("QAT","Austria"),
    ("BQF","Belgium"),
    ("ABRQ","Brasil"),
    ("QC","Canada"),
    ("AQC","Catalonia"),
    ("ACQ","Chile"),
    ("CAF","Czech Republic"),
    ("DQF","Denmark"),
    ("QF","Finland"),
    ("FQF","France"),
    ("DQB","Germany"),
    ("HKQA","Hong Kong"),
    ("QSÍ","Iceland"),
    ("QI","India"),
    ("QIRE","Ireland"),
    ("AIQ","Italy"),
    ("JQA","Japan"),
    ("QM","Malaysia"),
    ("QMX","México"),
    ("QNL","Netherlands"),
    ("QNZ","New Zealand"),
    ("NRF","Norway"),
    ("FDPQ","Peru"),
    ("PLQ","Poland"),
    ("QPt","Portugal"),
    ("QK","Korea"),
    ("QS","Serbia"),
    ("SQA","Slovakia"),
    ("QSVN","Slovenia"),
    ("AQE","Spain"),
    ("SvQF","Sweden"),
    ("SQV","Switzerland"),
    ("QD","Turkey"),
    ("QU","Uganda"),
    ("QUK","UK"),
    ("VQA","Vietnam"),
    ("Other","Not listed"),
)

TRANSFER_STATE_CHOICES =(
    ("r","Requested"),
    ("p","Pending Approval"),
    ("a","Approved"),
    ("o","Old"),
)

APPROVAL_CHOICES =(
    ("f","FROM APPROVED"),
    ("t","TO APPROVED"),
    ("l","LEAGUE APPROVED"),
    ("n","NGB APPROVED"),
)


class Team(models.Model):
    name = models.CharField(
        max_length=100,
    )
    ngb = models.CharField(choices=NGB_CHOICES, max_length=5)
    image = ImageField(_("Team Logo"), upload_to="team_logos", blank=True)
    members = models.ManyToManyField(User, through='Transfer', related_name='memberships')
    staff = models.ManyToManyField(User, through='Role', related_name='roles')

    @property
    def active_members(self):
        return User.objects.filter(
            transfers__to_team=self,
            transfers__state='a'
        )

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(
        max_length=100,
    )
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.team.name, self.player.first_name)


class Transfer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers')
    to_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='transfers')
    from_ngb = models.CharField(choices=NGB_CHOICES, max_length=5, null=True, blank=True)
    reason = models.TextField(max_length=512)
    state = models.CharField(choices=TRANSFER_STATE_CHOICES, max_length=1, default='r')
    approval = MultiSelectField(choices=APPROVAL_CHOICES, blank=True, null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.to_team.name, self.player.first_name, self.state)
