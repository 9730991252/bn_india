
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("websocket_connect", event)
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print("websocket_receive", event)
        print(event['text'])
        self.send({
            "type": "websocket.send",
            "text": "Message Sent to Client"
        })

    def websocket_disconnect(self, event):
        print("websocket_disconnected..", event)
        raise StopConsumer()
    
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket_connected...", event)
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("websocket_receive", event)
        print(event['text'])
        await self.send({
            "type": "websocket.send",
            "text": "Message Sent to Client"
        })

    async def websocket_disconnect(self, event):
        print("websocket_disconnected..", event)
        raise StopConsumer()