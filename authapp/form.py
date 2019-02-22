from django.contrib.auth.forms import UserCreationForm
from companiesapp.models import company
from django.forms import ModelForm


class RegisterCompany(UserCreationForm):
    fields = ["username", "email"]

class CompanyCreateForm(ModelForm):
    class Meta:
        model = company
        fields = ["voen", "name", "ceo_first_name", "ceo_last_name"]

