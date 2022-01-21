import stomp
# import time
import asyncio
import sys

class ClientStomp():
    def __init__(self, channel:str,message:str):
        self.conn = stomp.Connection([('localhost', 61613)])
        self.conn.connect('admin', 'admin', wait=True)
        self.channel = channel
        self.message = message

    async def send_event(self):
        try:
            print(f"Sending Topic Message : {self.message}")
            await asyncio.sleep(1)
            self.conn.ack(id=1,subscription=1)        
            self.conn.send(destination=self.channel, body=self.message)
        except Exception as e:
            print(f"Error processsing Topic message {e}")

    async def main(self):       
        task_send_event = asyncio.create_task(self.send_event())
        await task_send_event


if __name__ == "__main__":
    my_client = ClientStomp(sys.argv[1], sys.argv[2])
    asyncio.run(my_client.main())