from django.contrib import admin
from .models import Category, Question

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_new', 'description')
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'category', 'correct_index')
    list_filter = ('category',)
    search_fields = ('text',)
