from django.contrib import admin
from .models import Destination, Review

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'added_on')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('destination', 'user', 'rating', 'created_at')
