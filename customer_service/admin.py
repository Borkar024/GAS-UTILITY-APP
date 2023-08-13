from django.contrib import admin
from .models import ServiceRequest

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['customer_name','type','details','attached_file','submitted_at','resolved_at','status']
admin.site.register(ServiceRequest,ServiceAdmin)
