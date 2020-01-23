from django.contrib import admin
from .models import TodoListModel

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.
admin.site.register(TodoListModel)
