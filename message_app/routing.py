from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r'ws/socket-server/', consumers.chatConsumer.as_asgi()),
    # path(r'ws/socket-server/<str:room_name>', consumers.contactConsumer.as_asgi()),
    path(r'ws/socket-server/notification', consumers.notificationConsumer.as_asgi()),
]