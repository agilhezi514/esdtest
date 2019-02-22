from django.urls import path
from .views import *

urlpatterns = [
    path("register/", CompanyRegister.as_view(), name ="company_register"),
    path("login/", auth_login.as_view(), name = "login_page")
]