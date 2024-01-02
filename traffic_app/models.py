from django.db import models
# Create your models here.


class Point(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Path(models.Model):
    name = models.CharField(max_length=100)
    start_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='start_point')
    end_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='end_point')
    raw_time = models.FloatField()

    WEATHER_OFFSETS = {
        'sun': 1.0,
        'rain': 1.3,
        'snow': 1.8,
        'fog': 1.5,
    }

    TIME_PERIOD_OFFSETS = {
        '0-7': 0.9,
        '7-10': 1.8,
        '10-16': 1.2,
        '16-19': 1.8,
        '19-24': 1.0,
    }

    def calculate_real_travel_time(self, weather, time_period):
        weather_offset = self.WEATHER_OFFSETS.get(weather, 1.0)
        time_period_offset = self.TIME_PERIOD_OFFSETS.get(time_period, 1.0)

        return self.raw_time * weather_offset * time_period_offset

    def __str__(self):
        return f"{self.name} : {self.start_point} to {self.end_point}"


class Map(models.Model):
    vertices = models.ManyToManyField(Point)
    paths = models.ManyToManyField(Path)

    def __str__(self):
        return f"Map with {self.vertices.count()} vertices and {self.paths.count()} paths"



