import stomp
import asyncio
import sys
import configparser

class ClientStomp():
    def __init__(self, channel:str,message:str):
        """
            Create a new instance of the class ClientStomp, recive many parameters.

        """
        try:
            # import pdb;pdb.set_trace()

            self.config = configparser.ConfigParser()
            self.config.read('settings/config.ini')

            self.conn = stomp.Connection([(self.config.get('CLIENT','HOST'), self.config.get('CLIENT','PORT'))])
            self.conn.connect(self.config.get('CLIENT','USERNAME'), self.config.get('CLIENT','PASSWORD'), wait=True)

            self.channel = channel
            self.message = message
        except Exception as e:
            print(f'Error connecting to {e}')
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
    try:
        host = sys.argv[1]
        message  = sys.argv[2]

        my_client = ClientStomp(host, message)
        asyncio.run(my_client.main())
    except Exception as e:
        print(f"Error with the clien {e}")