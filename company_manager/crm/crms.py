from django.urls import path
import crm.views as views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("company/create", views.CompanyCreateView.as_view(), name="company_create"),
]
