from django.db import models
from django.contrib.auth.models import User

class company(models.Model):
    voen = models.IntegerField(verbose_name = "VOEN", unique = True)
    name = models.CharField(max_length=255, verbose_name = "Sirketin adi")
    ceo_first_name = models.CharField(max_length=50, verbose_name = "Sirketin rehberinin adi")
    ceo_last_name =models.CharField(max_length=50, verbose_name = "Sirketin rehberinin soyadi")
    user = models.OneToOneField(User, on_delete = models.CASCADE)


class AsanImza(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    asan_imza = models.IntegerField("Asan Imza", unique = True)
    asan_nomre = models.CharField("Asan Nomre", max_length=20, unique = True)

class CompanyContracts(models.Model):
    __choice = ((1, "Telefon"),
    (2, "Email"),
    (3, "Adsress"))
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    contact_type = models.IntegerField(choices = __choice)
    contact = models.CharField(max_length=255, verbose_name = "Elaqe")