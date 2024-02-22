from django.db.models.base import Model as Model
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,View,UpdateView
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm,UserEditForm,CustomPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from URLShorten.Utils.utils import GuestOnlyMixin
from django.contrib.auth.views import PasswordChangeView

class DashboardView(LoginRequiredMixin,TemplateView):
    login_url = "/login"
    template_name = "dashboard.jinja"


class IndexView(TemplateView):
    template_name = "index.jinja"

class RegisterView(GuestOnlyMixin,CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register.jinja'
    success_url = reverse_lazy('success_page')

class LogoutView(LoginRequiredMixin,View):
    login_url = "/login"
    def get(self,req):
        logout(req)
        return redirect("/")

class UserUpdateView(UpdateView):
    model = User
    form_class = UserEditForm
    success_url = "/dashboard"
    template_name = "useredit.jinja"
    def get_object(self, queryset=None):
        user = super().get_object(queryset=queryset)
        if self.request.user.id != user.id:
            raise PermissionDenied()
        return user
    
class LogView(GuestOnlyMixin,LoginView):
    template_name="login.jinja"
    next_page = "/"
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the home page or any desired page
        else:
            messages.error(request, 'Invalid login credentials.',"alert alert-danger list-unstyled")
            return render(request, 'login.jinja')

class UserPasswordUpdateView(PasswordChangeView):
    model = User
    form_class = CustomPasswordChangeForm
    success_url = "/dashboard"
    template_name = "passwordedit.jinja"