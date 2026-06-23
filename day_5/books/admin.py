from django.contrib import admin
from .models import Book, Category, ISBN

class ISBNInline(admin.StackedInline):
    model = ISBN
    extra = 0
    can_delete = False
    max_num = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rate', 'views')
    list_filter = ('user', 'categories')
    search_fields = ('title', 'desc')
    inlines = [ISBNInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ISBN)
class ISBNAdmin(admin.ModelAdmin):
    list_display = ('isbn_number', 'book_title', 'author_title', 'book')
    search_fields = ('isbn_number', 'book_title', 'author_title')
    