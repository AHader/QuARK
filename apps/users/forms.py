from django.contrib.auth import get_user_model, forms
from django.forms import ModelForm, DateInput
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class CustomSignupForm(ModelForm,SignupForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "birthdate", "citizenship", "gender", "positions", "certifications"]
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'})
        }

    def custom_signup(self, request, user):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthdate = self.cleaned_data['birthdate']
        user.citizenship = self.cleaned_data['citizenship']
        user.gender = self.cleaned_data['gender']
        user.positions = self.cleaned_data['positions']
        user.certifications = self.cleaned_data['certifications']
        user.save()
        return user
