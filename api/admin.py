from django.contrib import admin
from .models import Meal, Rating

# Register your models here.
class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['name']
    search_fields = ['name']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal', 'auth', 'stars']
    list_filter = ['meal', 'auth']


admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)