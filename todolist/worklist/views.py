from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib import messages

from .forms import ListForm
from .models import TodoListModel

# Create your views here.


def index(request):
    return render(request, "worklist/index.html")


def TodoList(request):
    if request.method == 'GET':
        form = ListForm(request.GET)
        if form.is_valid():
            form.save()
            return ThingsToDo(request)
        else:
            # messages.error(request, print(
                # f"Please enter within {TodoListModel.title()} charecter"))
            return HttpResponseRedirect("worklist/index.html")
    else:
        form = ListForm
        return HttpResponseRedirect("worklist/index.html")


def ThingsToDo(request):
    query_list = TodoListModel.objects.all()
    return render(request, 'worklist/redirect.html', {'query_list': query_list})
