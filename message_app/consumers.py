import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from .models import conversation
import asyncio

class chatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_group_name = 'chats'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        asyncio.create_task(self.continuous_fetching_data())

        print('Connected...')
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        print('Connection closed...', close_code)

    async def receive(self, text_data):
        pass
        # await self.continuous_fetching_data(text_data) 

        # text_data_json = json.loads(text_data)
        # msg = text_data_json['message']
        # sender = text_data_json['user']
        # receiver = text_data_json['receiver']
        # profileUrl = text_data_json['profileUrl']
        # convoId = text_data_json['convoId']

        # new_message = conversation.objects.create(
        #     convo_id = convoId,
        #     message_content = msg,
        #     sender = sender,
        #     receiver = receiver,
        #     status = 'sent',
        # )

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
    
    async def continuous_fetching_data(self):
        while True:
            data = await sync_to_async(self.fetch_data_from_db)()
            # for i in data:
            #     msg = i['sender']
            #     print(msg)

            await self.send(text_data=json.dumps({
                'data': data
            }))

            await asyncio.sleep(1)

    
    def fetch_data_from_db(self):
        data = conversation.objects.all().values('message_content', 'sender')

        return list(data)

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