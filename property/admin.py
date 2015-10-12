from django.contrib import admin
from .models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'bathrooms', 'bedrooms', 'kitchens')
    list_filter = ('bathrooms', 'bedrooms', 'kitchens',)
    search_fields = ('title',)


admin.site.register(House, HouseAdmin)
