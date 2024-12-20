import json

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from .models import conversation, message, users, notification

# ~~~~~~~~~~ Websocket Connection ~~~~~~~~~~ #

# Chats
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

        convoId = text_data_json['convo_id']
        msg = text_data_json['message']
        user = text_data_json['user']
        rcvr = text_data_json['receiver']

        await self.insert_message_to_db(convoId, msg, user, rcvr)
        fetched_data = await self.fetching_data(user)

        username = fetched_data['user']['username']
        profile_url = fetched_data['user']['profile_url']

        msg = fetched_data['convo']['message_content']
        sender = fetched_data['convo']['sender']
        receiver = fetched_data['convo']['receiver']
        convo_id = fetched_data['convo']['convo_id']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'convo_id': convo_id,
                'msg_content': msg,
                'sender': sender,
                'receiver': receiver,

                'username': username,
                'profile_url': profile_url,
            }
        )

    async def chat_message(self, event):
        message_content = event['msg_content']
        convo_id = event['convo_id']
        sender = event['sender']

        username = event['username']
        profile_url = event['profile_url']


        await self.send(text_data=json.dumps({
            'type': 'new_chat',
            'message_content': message_content,
            'convo_id': convo_id,
            'sender': sender,
            
            'username': username,
            'profile_url': profile_url,
        }))
    
    async def fetching_data(self, user):
        fetched_convo = await database_sync_to_async(self.fetch_data_from_convo)()
        fetched_user = await database_sync_to_async(self.fetch_data_from_user)(user)

        fetched_data = {}

        if fetched_convo:
            fetched_data['convo'] = {
                'type': 'new_chat',
                'message_content_id': fetched_convo.message_content_id,
                'message_content': fetched_convo.message_content,
                'convo_id': fetched_convo.convo_id,
                'sender': fetched_convo.sender,
                'receiver': fetched_convo.receiver,
                'status': fetched_convo.status,
                'created_at': str(fetched_convo.created_at),
            }
        
        if fetched_user:
            fetched_data['user'] = {
                'type': 'users',
                'username': fetched_user.username,
                'profile_url': str(fetched_user.profile.url),
            }

        return fetched_data
    
    def fetch_data_from_user(self, user):
        return users.objects.filter(username = user).first()
    
    def fetch_data_from_convo(self):
        return conversation.objects.order_by('created_at').last()
    
    @database_sync_to_async
    def insert_message_to_db(self, convoId, msg, user, rcvr):
        conversation.objects.create(
            convo_id = convoId,    
            message_content = msg,
            sender = user,
            receiver = rcvr,
            status = 'sent',
        )
        
# Notifications
class notificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'notification'

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

        type = text_data_json['type']

        if (type == 'send'):
            req_from = text_data_json['req_from']
            req_to = text_data_json['req_to']

            await self.insert_notif_to_db(req_from, req_to)
        else:
            req_to = text_data_json['req_to']

            await self.remove_req_to_db(req_to)

    @database_sync_to_async
    def insert_notif_to_db(self, req_from, req_to):
        notification.objects.create(
            message_content = 'Sends you a friend request',
            request_from = req_from,
            request_to = req_to,
        )
    
    @database_sync_to_async
    def remove_req_to_db(self, req_to):
        notification.objects.filter(request_to = req_to).delete()