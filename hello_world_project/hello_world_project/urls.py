from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world_app/', include('hello_world_app.urls')),
]
