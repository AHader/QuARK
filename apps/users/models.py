from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField
from imagefield.fields import ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from multiselectfield import MultiSelectField
from django_countries.fields import CountryField

Position_CHOICES =(
    ("C", "Chaser"),
    ("K", "Keeper"),
    ("B", "Beater"),
    ("S", "Seeker"),
)

Certification_CHOICES =(
    ("A", "Assistent Ref"),
    ("S", "Snitch Ref"),
    ("H", "Head Ref"),
)

Gender_CHOICES =(
    ("M", _("Male")),
    ("F", _("Female")),
    ("N", _("Non-Binary")),
)

class User(AbstractUser):
    phone_number = CharField(max_length=256, blank=True, null=True)
    birthdate = DateField(_("Date of birth"))
    citizenship = CountryField(blank_label='(select citizenship)')
    avatar = ImageField(_("avatar"), upload_to="avatars", blank=True, auto_add_fields=True,
                        formats={
                            "thumb": ["default", ("crop", (240, 300))],
                            "desktop": ["default", ("thumbnail", (500, 500))],
                        })
    gender = CharField(choices=Gender_CHOICES, max_length=1)
    positions = MultiSelectField(choices=Position_CHOICES)
    certifications = MultiSelectField(choices=Certification_CHOICES)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"id": self.id})
