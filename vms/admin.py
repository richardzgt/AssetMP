from django.contrib import admin
from models import *

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name','host','describe')

class VmsAdmin(admin.ModelAdmin):
    list_display = ('vmname','owner','status')
    # def log_change(self, request, objec


admin.site.register(Template,TemplateAdmin)
admin.site.register(Vms,VmsAdmin)