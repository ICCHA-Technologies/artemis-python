import stomp
import asyncio
import sys
import configparser

class ClientStomp():
    def __init__(self, channel:str,message:str):
        """
            Create a new instance of the class ClientStomp, recive many parameters.

        """
        config = configparser.ConfigParser()
        config.read('settings/config.ini')
        self.conn = stomp.Connection([(config.get('CLIENT','HOST'), config.get('CLIENT','PORT'))])
        self.conn.connect(config.get('CLIENT','USERNAME'), config.get('CLIENT','PASSWORD'), wait=True)
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

    #Client send message in the queue architecture
    async def producer_message(self):
        try:
            print(f"Sending Queue Message : {self.message}")
            await asyncio.sleep(1)
            # self.conn.ack(id=1,subscription=1)        
            self.conn.send(destination=self.channel, body=self.message)
        except Exception as e:
            print(f"Error processsing Queue message {e}")

    #Client send message in the topic architecture
    async def publisher_message(self):
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