from django.shortcuts import render
from .models import Map, Point

# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def map_view(request):
    map_instance = Map.objects.first()
    vertices = map_instance.vertices.all()
    paths = map_instance.paths.all()

    return render(request, 'map.html', {'vertices': vertices, 'paths': paths})


def calculate_best_way(request):
    map_instance = Map.objects.first()  # Assuming you have only one map in the database
    vertices = map_instance.vertices.all()

    if request.method == 'POST':
        start_point_id = request.POST.get('start_point')
        end_point_id = request.POST.get('end_point')

        start_point = Point.objects.get(id=start_point_id)
        end_point = Point.objects.get(id=end_point_id)

        # Perform the calculation for the best way
        best_way = map_instance.get_fastest_path(start_point, end_point, 'sun', '19-24')

        return render(request, 'way_result.html', {'start_point': start_point, 'end_point': end_point, 'best_way': best_way})

    return render(request, 'way.html', {'vertices': vertices})