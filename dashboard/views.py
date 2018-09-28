from django.views.generic import TemplateView


class DashboardView(TemplateView):
    # template_name = "pages/dashboard.html"
    template_name = "pages/dashboard.html"

class LoginView(TemplateView):
    template_name = "pages/login.html"