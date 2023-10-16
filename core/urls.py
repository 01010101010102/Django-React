from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Home/', include("Home.urls")),
    path('Creators/', include("Creators.urls")),
    path('admin/', admin.site.urls),
]
