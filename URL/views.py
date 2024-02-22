from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView,DetailView,ListView,View
from .models import *
from .forms import URLForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
# Create your views here.

class URLRedirectView(View):
    def get(self,request,*args,**kwargs):
        ip = None
        if request.META.get('HTTP_X_FORWARDED_FOR') != None:
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
        elif request.META.get('HTTP_CLIENT_IP'):
            ip = request.META.get('HTTP_CLIENT_IP')
        else:
            ip = request.META.get("REMOTE_ADDR")
        user_agent = request.META['HTTP_USER_AGENT']
        slug = kwargs["slug"]
        url = URL.objects.get(slug=slug)
        inst = IP.objects.create(ip=ip,user_agent=user_agent,linked_url=url)
        return redirect(url.url)



class URLSIndex(LoginRequiredMixin,ListView):
    login_url = "/login"
    template_name="urlslist.jinja"
    model = URL
    context_object_name = "urls"
    def get_queryset(self) -> QuerySet[Any]:
        data = self.model.objects.filter(user_id=self.request.user.id)
        return data

class URLDetails(LoginRequiredMixin,DetailView):
    login_url = "/login"
    template_name = "urldetails.jinja"
    model = URL
    def get_object(self, queryset=None):
        url = super().get_object(queryset=queryset)
        if url.user_id != self.request.user:
            raise PermissionDenied()
        return url

class URLCreateView(LoginRequiredMixin,CreateView):
    login_url = "/login"
    model = URL
    form_class = URLForm
    template_name = 'urlcreate.jinja'
    user_field = "user_id"
    def form_valid(self, form):
        setattr(form.instance, self.user_field, self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('url_detail', kwargs={'slug': self.object.slug})
    