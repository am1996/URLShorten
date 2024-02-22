from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('dashboard/',DashboardView.as_view()),
    path('login/',LogView.as_view()),
    path('success_page/',TemplateView.as_view(template_name="success_page.jinja")),
    path("register/",RegisterView.as_view()),
    path("aboutus/",TemplateView.as_view(template_name="aboutus.jinja") ),
    path("logout/",LogoutView.as_view()),
    path("urls/", include("URL.urls"),name="urls"),
    path("edituser/<int:pk>/",UserUpdateView.as_view()),
    path("changepassword/",UserPasswordUpdateView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
