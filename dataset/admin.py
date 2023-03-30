from django.contrib import admin
from .models import Movies

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category' , 'trailer_URL')

admin.site.register(Movies, MovieAdmin)
