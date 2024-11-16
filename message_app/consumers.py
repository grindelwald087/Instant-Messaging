import json
import asyncio
import random
import string

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from .models import conversation

class chatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_group_name = 'chats'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        print('Connected...')
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        print('Connection closed...', close_code)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json['message']

        await self.insert_message_to_db(msg)
        await self.fetching_data()

        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': msg,
        #         'sender': sender,
        #         'receiver': receiver,
        #         'profileUrl': profileUrl,
        #         'convoId': convoId,
        #     }
        # )
    
    async def fetching_data(self):
        fetched = await database_sync_to_async(self.fetch_data_from_db)()

        if fetched:
            serialized_data = {
                'type': 'new_chat',
                'message_content_id': fetched.message_content_id,
                'message_content': fetched.message_content,
                'convo_id': fetched.convo_id,
                'sender': fetched.sender,
                'receiver': fetched.receiver,
                'status': fetched.status,
                'created_at': str(fetched.created_at),
            }

            await self.send(text_data=json.dumps(serialized_data))
    
    def fetch_data_from_db(self):
        return conversation.objects.order_by('created_at').last()
    
    @database_sync_to_async
    def insert_message_to_db(self, msg):
        # convo_id = chatConsumer.generate_random_convo_id(15)

        conversation.objects.create(
            convo_id = 10,    
            message_content = msg,
            sender = 'bastard_11',
            receiver = 'no_one_12',
            status = 'sent',
        )
    
    # @staticmethod
    # def generate_random_convo_id(length = 8):
    #     characters = string.ascii_letters + string.digits
        
    #     random_id = ''.join(random.choices(characters, k=length))
        
    #     return random_id
    
    # def chat_message(self, event):
    #     msg = event['message']
    #     sender = event['sender']
    #     receiver = event['receiver']
    #     profileUrl = event['profileUrl']
    #     convoId = event['convoId']

    #     self.send(text_data=json.dumps({
    #         'type': 'chats',
    #         'message': msg,
    #         'sender': sender,
    #         'receiver': receiver,
    #         'profile_url': profileUrl,
    #         'convoId': convoId,
    #     }))