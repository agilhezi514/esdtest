from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .form import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import Group, Permission
from django.db.models import Q

class CompanyRegister(TemplateView):
    template_name = "register.html"

    def get_group(self):
        try:
            return Group.objects.get(name = "company")
        except Group.DoesNotExist:
            company_group = Group.objects.create(name = "company")
            
            permissions = Permission.objects.filter(Q(codename="view_company") | Q(codename="update_company") | Q(codename__icontains="asan") | Q(codename__icontains="document") | Q(codename__icontains="contact"))

            for p in permissions:
                company_group.permissions.add(p)
            
            return company_group           


    def get_context_data(self):
        context = super().get_context_data()
        context['userform'] = RegisterCompany
        context["companyform"] = CompanyCreateForm
        return context
    
    def post(self, request, *args, **kwargs):
        new_user = RegisterCompany(request.POST)
        new_company = CompanyCreateForm(request.POST)
        if new_user.is_valid() and new_company.is_valid():
            group = self.get_group()

            new_user = new_user.save(commit = True)
            new_company.instance.user = new_user
            new_company.save()
            new_user.save()

            group.user_set.add(new_user)

            return redirect("login_page")

        else:
            context = self.get_context_data()
            context['userform'] = new_user
            context["companyform"] = new_company

            return render(request, self.template_name, context)

        
class auth_login(LoginView):
    template_name = "login.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get("next"):
            context['redirect_to'] = self.request.GET.get('next')
        else:
            context['redirect_to'] = "/"

        return context

    
