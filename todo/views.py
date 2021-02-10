from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item.name')
        done = 'done' in request.POST

    return render(request, 'todo/add_item.html')
