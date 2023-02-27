from django.contrib import admin
from .models import *

#----------------[ Show models ]----------------#
class AdminSubject(admin.ModelAdmin):
    list_display=('s_id','name','short_desc','icon','is_paid',)
    search_fields=('name',)
    list_filter=('name',)

class AdminUnit(admin.ModelAdmin):
    list_display = ('u_id','uname','u_description','u_video','image_format',)
    search_fields=('uname',)
    list_filter = ('uname',)

#----------------[ Register models here ]----------------#
admin.site.register(Subject,AdminSubject)
admin.site.register(Unit,AdminUnit)