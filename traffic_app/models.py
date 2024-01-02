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

    def __str__(self):
        return f"{self.name} : {self.start_point} to {self.end_point}"


class Map(models.Model):
    vertices = models.ManyToManyField(Point)
    paths = models.ManyToManyField(Path)

    def __str__(self):
        return f"Map with {self.vertices.count()} vertices and {self.paths.count()} paths"
