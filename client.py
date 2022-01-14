import stomp
import time
import asyncio
import random

class ClientStomp():
    def __init__(self):
        self.conn = stomp.Connection([('localhost', 61613)])
        self.conn.connect('admin', 'admin', wait=True)

    async def send_message_topic(self, new_message):
        print(f"Sending Topic Message : {new_message}")
        await asyncio.sleep(1)
        self.conn.send('A.B.C.D', new_message)


    async def send_message_queue(self, new_message):       
        print(f"Sending Queue Message: {new_message}")
        await asyncio.sleep(1)
        self.conn.send('/queue/test', new_message)


    async def main():
        task1 = asyncio.create_task(send_message_queue(''))
        await task1

        task2 = asyncio.create_task(send_message_topic(''))
        await task2

