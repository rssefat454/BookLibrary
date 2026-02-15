from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'category', 'published_date')
    list_filter = ('status', 'category')
    search_fields = ('title', 'author')
