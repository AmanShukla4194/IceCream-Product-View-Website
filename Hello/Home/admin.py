from django.contrib import admin
# from Home.models import *   for all models
from Home.models import Contact
from Home.models import LogIns

# Register your models here.

# admin.site.register(Contact)    # apne model ko register karna hai yaha pe admin me
# fir apne aaps.py se settings me installed apps me use daal dena hai

admin.site.register(Contact)
admin.site.register(LogIns)

# @admin.register(Contact)
# class admins(admin.ModelAdmin):
#     list_display = ["name","phone","email","desc","date"]
    
# @admin.register(LogIns)
# class LogIns(admin.ModelAdmin):
#     list_display = ["username","password"]
    
  










