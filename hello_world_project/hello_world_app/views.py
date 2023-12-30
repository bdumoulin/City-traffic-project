from django.shortcuts import render
from .models import Message


def hello_world(request):
    message = Message.objects.create(content="Hello World!")
    return render(request, 'hello_world.html', {'message': message})
