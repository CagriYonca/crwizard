from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
import requests

# Create your views here.
def todoView(request):
    all_items = TodoItem.objects.all()
    return render(request, 'todo.html', 
        {'all_items': all_items})

def addTodo(request):
    url = request.POST['link']
    # xml_file = requests.get(url)
    # with open('file.xml', 'wb') as f:
    #     f.write(xml_file.content)
    new_item = TodoItem(content=url)
    new_item.save()

    return HttpResponseRedirect('/todo/')
    # create a new todo all_items object
    # save
    # redirect the browser to '/todo/'

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')    
