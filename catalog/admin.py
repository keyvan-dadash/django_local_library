from django.contrib import admin
from .models import *
@admin.register(Author,Book,BookInstance,Genre)
class AdminAuthor(admin.ModelAdmin):
    pass
