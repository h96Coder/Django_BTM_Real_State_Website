from django.contrib import admin
from .models import Realtor
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','is_mvp')
    list_display_links = ('name',)
    search_fields = ('name','email','phone')
    list_filter =('name',)
    list_editable = ('is_mvp',)
admin.site.register(Realtor,RealtorAdmin)



# Register your models here.
