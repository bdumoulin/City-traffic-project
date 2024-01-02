from django.contrib import admin

# Register your models here.

from .models import Point, Path

admin.site.register(Point)
admin.site.register(Path)
