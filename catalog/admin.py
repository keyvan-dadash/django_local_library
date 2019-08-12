from django.contrib import admin
from .models import *


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
    fields = ('first_name','last_name',('date_of_birth','date_of_death'))

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','due_back')
    list_display = ('id', 'status', 'book', 'borrower', 'due_back')
    fieldsets = (
    ('Information', {'fields': ('book', 'imprint', 'id')}),
    ('Availability',{'fields': ('status', 'due_back', 'borrower')})
    )

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BookInstanceInline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
