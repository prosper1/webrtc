from django.urls import re_path
from .consumers import ConferenceConsumer


websocket_urlpatterns = [
    re_path(r'ws/conference_room/(?P<room_name>\w+)/$',ConferenceConsumer),
]