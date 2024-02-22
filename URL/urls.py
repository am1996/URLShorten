from django.contrib import admin
from django.urls import path
from .views import *

namespace="URL"

urlpatterns = [
    path("",URLSIndex.as_view()),
    path("create/",URLCreateView.as_view(),name="url_create"),
    path("<slug:slug>/",URLRedirectView.as_view(),name="url_detail"),
    path("<slug:slug>/details/",URLDetails.as_view(),name="url_detail")
]
