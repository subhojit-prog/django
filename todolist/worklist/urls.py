from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data/", views.TodoList, name="adata"),
    path("list/", views.ThingsToDo, name="Things to-do"),
    # path("admin/", admin.site.urls)
]
