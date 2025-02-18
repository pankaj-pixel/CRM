from django.contrib import admin
from . models import Leads,comments,LeadFiles

# Register your models here.
admin.site.register(Leads)
admin.site.register(comments)
admin.site.register(LeadFiles)