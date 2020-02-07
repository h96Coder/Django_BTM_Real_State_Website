from django.contrib import admin
from .models import Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','city','state','zipcode','price')
    list_display_links = ('id','title')
    list_editable =('is_published',)
    list_filter = ('realtors',)
    search_fields = ('title','address','city')
admin.site.register(Listing,ListingAdmin)
# Register your models here.
