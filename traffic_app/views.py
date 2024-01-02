from django.shortcuts import render

# Create your views here.

from .models import Map


def map_view(request):
    map_instance = Map.objects.first()  # Assuming you have only one map in the database
    vertices = map_instance.vertices.all()
    paths = map_instance.paths.all()

    return render(request, 'map.html', {'vertices': vertices, 'paths': paths})
