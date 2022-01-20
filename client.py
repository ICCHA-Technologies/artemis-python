import stomp
import time
import asyncio
import random

class ClientStomp():
    def __init__(self):
        self.conn = stomp.Connection([('localhost', 61613)])
        self.conn.connect('admin', 'admin', wait=True)
        # self.conn.ack(id=1, subscription=1)        
        # self.conn.ack(id=2, subscription=2)        


    async def send_message_topic(self, new_message):
        try:
            print(f"Sending Topic Message : {new_message}")
            await asyncio.sleep(1)
            self.conn.ack(id=1,subscription=1)        
            self.conn.send(destination='/topic/test', body=new_message)
        except Exception as e:
            print(f"Error processsing Topic message {e}")


    async def send_message_queue(self, new_message):       
        try:
            print(f"Sending Queue Message: {new_message}")
            await asyncio.sleep(1)
            self.conn.ack(id=2,subscription=2)        
            self.conn.send(destination='/queue/test', body=new_message)
        except Exception as e:
            print(f"Error processsing Queue message {e}")

    async def main():       
        task1 = asyncio.create_task(send_message_queue())
        await task1

        task2 = asyncio.create_task(send_message_topic())
        await task2

