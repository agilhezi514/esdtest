from django.shortcuts import render
from django.views.generic import TemplateView
from .models import company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from braces.views import PermissionRequiredMixin

class Company_view(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "companypage.html"
    login_url = reverse_lazy("login_page")
    permission_required = "companiesapp.view_company"
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        company_info = company.objects.get(user= self.request.user)
        context["company_info"] = company_info
        return context

    

    
