from django import forms
from django.forms import ModelForm

from .models import TodoListModel


class ListForm(forms.ModelForm):

    class Meta:
        model = TodoListModel
        fields = "__all__"
