from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Category

from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
    )

# Create your views here.

def index(request, *args, **kwargs):
    todos = TodoList.objects.all()
    categories = Category.objects.all()

    context = {
        'todos' : todos,
        'categories' : categories
    }

    if request.method =='POST':
        if 'taskAdd' in request.POST:
            title = request.POST['title']
            category = request.POST['category_select']
            date = request.POST['date']
            content = title + " -- " + date + " " + category
            Todo = TodoList(title= title, content = content, due_date = date, category = Category.objects.get(name=category))
            Todo.save()
            return redirect('/')

        if 'taskDelete' in request.POST:
            checkedList = request.POST.get("checkedBox")
            print(checkedList)
            Id = request.POST['todoItem'];
            print(Id)
            todoDel = TodoList.objects.get(id = int(Id))
            todoDel.delete()
            return redirect('/')

        if 'taskDeleteAll' in request.POST:
            TodoList.objects.all().delete()
            return redirect('/')


    return render(request, "index.html", context)


