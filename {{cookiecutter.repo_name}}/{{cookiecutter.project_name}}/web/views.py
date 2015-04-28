from django.views.generic import TemplateView, FormView, DetailView
from django.contrib.auth import authenticate, login
from django.conf import settings

import logging

from .forms import RegisterForm
from .models import UserProfile
from .mixins import PageTitleMixin, StatusContextMixin, LoggedInMixin

User = settings.AUTH_USER_MODEL
logger = logging.getLogger("print-debug")


class BaseOutsideView(PageTitleMixin, StatusContextMixin):
    pass


class BaseInsideView(PageTitleMixin, LoggedInMixin, StatusContextMixin):
    pass


class RegisterView(FormView, BaseOutsideView):
    template_name = 'registration/main.html'
    form_class = RegisterForm
    success_url = '/dashboard/'
    title = "Register"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        logged_in_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        login(self.request, logged_in_user)
        return super(RegisterView, self).form_valid(form)


class DashboardView(DetailView, BaseInsideView):
    template_name = "inside/dashboard.html"
    model = UserProfile
    title = "Dashboard"


class SettingsView(FormView, BaseInsideView):
    template_name = "inside/dashboard.html"
    model = UserProfile
    title = "User Settings"
