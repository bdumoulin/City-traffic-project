from django.db import models
from collections import defaultdict, namedtuple
import matplotlib.pyplot as plt
import networkx as nx
import heapq
# Create your models here.


class Point(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __hash__(self):
        return hash(self.name)


class Path(models.Model):
    name = models.CharField(max_length=100)
    start_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='start_point')
    end_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='end_point')
    raw_time = models.FloatField()
    popularity_coeff = models.FloatField()

    current_time = models.FloatField()

    WEATHER_OFFSETS = {
        'sun': 1.0,
        'rain': 1.3,
        'snow': 1.8,
        'fog': 1.5,
    }

    TIME_PERIOD_OFFSETS = {
        '0-7': 0.8,
        '7-10': 1.6,
        '10-16': 1.1,
        '16-19': 1.6,
        '19-24': 1.0,
    }

    #  Method to modify to augment complexity of time in road
    #  MUST RETURN A FLOAT REPRESENTING THE REAL TIME
    #  The model can be modified as long as this function exists
    def calculate_real_travel_time(self, weather, time_period):
        weather_offset = self.WEATHER_OFFSETS.get(weather, 1.0)

        time_period_offset = self.TIME_PERIOD_OFFSETS.get(self.get_time_period(), 1.0)

        spent_time = self.raw_time * weather_offset * (time_period_offset * self.popularity_coeff)
        self.current_time = self.current_time + spent_time

        return spent_time

    def get_time_period(self):
        if self.current_time < 7:
            return '0-7'
        if 7 <= self.current_time < 10:
            return '7-10'
        if 10 <= self.current_time < 16:
            return '10-16'
        if 16 <= self.current_time < 19:
            return '16-19'
        if 19 <= self.current_time:
            return '19-24'

    def __str__(self):
        return f"{self.name} : {self.start_point} to {self.end_point}"


class Map(models.Model):
    vertices = models.ManyToManyField(Point)
    paths = models.ManyToManyField(Path)

    #  using djikstra's algorithm to get the fastest path from start to end
    def get_fastest_path(self, start_point, end_point, weather, time_period):
        graph = defaultdict(list)

        for path in self.paths.all():
            # Add edges for both directions in an undirected graph
            graph[path.start_point].append((path.end_point, path.calculate_real_travel_time(weather, time_period)))
            graph[path.end_point].append((path.start_point, path.calculate_real_travel_time(weather, time_period)))

        Edge = namedtuple('Edge', ['weight', 'vertex', 'path'])
        heap = [Edge(0, start_point, [start_point])]
        visited = set()

        while heap:
            current_edge = heapq.heappop(heap)
            current_weight, current_vertex, current_path = current_edge.weight, current_edge.vertex, current_edge.path

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            if current_vertex == end_point:
                return current_path

            for neighbor, weight in graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(heap, Edge(current_weight + weight, neighbor, current_path + [neighbor]))

        return None  # If no path found

    def __str__(self):
        return f"Map with {self.vertices.count()} vertices and {self.paths.count()} paths"



