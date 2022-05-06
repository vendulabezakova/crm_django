from django.views.generic import CreateView, ListView, TemplateView
import crm.models as models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class IndexView(TemplateView):
    template_name = "index.html"

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = models.Company
    template_name = "company/create_company.html"
    fields = ["name", "status", "phone_number", "email", "identification_number"]
    success_url = reverse_lazy("index")

class OpportunityCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "crm.add_opportunity"
    model = models.Opportunity
    template_name = "opportunity/create_opportunity.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("index")

class CompanyListView(LoginRequiredMixin, ListView):
    model = models.Company
    template_name = "company/company_list.html"
