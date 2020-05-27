from asgiref.sync import async_to_sync,sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
import json


class ConferenceConsumer(AsyncWebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(self.scope)
        self.room_group_name = 'room_%s' % self.room_name

        # Join group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to delivery group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'delivery_message',
                'message': message
            }
        )

    # Receive message from delivery group
    def delivery_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))