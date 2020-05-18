from django.contrib import admin
from .models import TodoList, Category
# Register your models here.

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created', 'due_date', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']