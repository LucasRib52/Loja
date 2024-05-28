from django.contrib import admin
from stores.models import Store, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('item', 'brand', 'model_year', 'value', 'description')
    search_fields = ('item', 'brand')
    
admin.site.register(Store, StoreAdmin)
admin.site.register(Brand, BrandAdmin)
