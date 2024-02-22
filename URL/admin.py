from django.contrib import admin
from .models import URL,IP

class URLAdmin(admin.ModelAdmin):
    pass

class IPAdmin(admin.ModelAdmin):
    pass

admin.site.register(IP,IPAdmin)
admin.site.register(URL, URLAdmin)