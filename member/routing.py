from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
]