from django.urls import path, include
from .views import (
    room
)

urlpatterns = [
    path('videogroup/<slug:room_name>/',room,name="room"),
]