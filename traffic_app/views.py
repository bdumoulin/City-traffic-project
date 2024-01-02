from django.shortcuts import render
from .models import Map, Point

# Create your views here.


def map_view(request):
    map_instance = Map.objects.first()
    vertices = map_instance.vertices.all()
    paths = map_instance.paths.all()

    path_data = [{'path': p, 'time': p.calculate_real_travel_time('rain', '7-10')} for p in paths]

    return render(request, 'map.html', {'vertices': vertices, 'path_data': path_data})


def calculate_best_way(request):
    map_instance = Map.objects.first()  # Assuming you have only one map in the database
    vertices = map_instance.vertices.all()

    if request.method == 'POST':
        start_point_id = request.POST.get('start_point')
        end_point_id = request.POST.get('end_point')

        start_point = Point.objects.get(id=start_point_id)
        end_point = Point.objects.get(id=end_point_id)

        # Perform the calculation for the best way
        best_way = map_instance.get_fastest_path(start_point, end_point, 'rain', '7-10')

        return render(request, 'way_result.html', {'start_point': start_point, 'end_point': end_point, 'best_way': best_way})

    return render(request, 'way.html', {'vertices': vertices})