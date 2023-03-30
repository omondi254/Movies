from django.contrib import admin
from .models import Movies

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

admin.site.register(Movies, MovieAdmin)
