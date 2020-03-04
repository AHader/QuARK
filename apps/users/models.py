from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import CharField, DateField, EmailField, IntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from multiselectfield import MultiSelectField
from django_countries.fields import CountryField
from sorl.thumbnail import ImageField

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


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    phone_number = CharField(max_length=256, blank=True, null=True)
    birthdate = DateField(_("Date of birth"), blank=True, null=True)
    citizenship = CountryField(blank_label='(select citizenship)', blank=True, null=True)
    image = ImageField(_("Player profile image"), upload_to="avatars", blank=True)
    gender = CharField(choices=Gender_CHOICES, max_length=1, blank=True, null=True)
    number = IntegerField(blank=True, null=True)
    positions = MultiSelectField(choices=Position_CHOICES, blank=True, null=True)
    certifications = MultiSelectField(choices=Certification_CHOICES, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"id": self.id})

    @property
    def team(self):
        return self.transfers.get(state='a').to_team

    @property
    def is_new(self):
        return self.team is None
