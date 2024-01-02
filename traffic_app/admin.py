from django.contrib import admin

# Register your models here.

from .models import Point, Path, Map

admin.site.register(Point)
admin.site.register(Path)
admin.site.register(Map)
