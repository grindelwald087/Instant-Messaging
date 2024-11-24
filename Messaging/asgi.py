import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import message_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Messaging.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter (
            message_app.routing.websocket_urlpatterns
        )
    )
})