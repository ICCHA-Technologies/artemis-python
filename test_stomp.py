# import client
import threading
import asyncio


from client import ClientStomp

my_client1 = ClientStomp()
my_client2 = ClientStomp()
my_client3 = ClientStomp()
my_client4 = ClientStomp()


asyncio.run( my_client1.send_message_queue("Client Queue 1 Hola Mundo!"))
asyncio.run( my_client2.send_message_topic("Client Topic 1 Hola Mundo!"))
asyncio.run( my_client3.send_message_queue("Client Queue 2 Hola Mundo!"))
asyncio.run( my_client4.send_message_topic("Client Topic 2 Hola Mundo!"))
asyncio.run( my_client3.send_message_queue("Client Queue 3 Hola Mundo!"))
asyncio.run( my_client4.send_message_topic("Client Topic 3 Hola Mundo!"))

asyncio.run( my_client3.send_message_queue("Client Queue 4 Hola Mundo!"))
asyncio.run( my_client3.send_message_queue("Client Queue 5 Hola Mundo!"))
asyncio.run( my_client3.send_message_queue("Client Queue 6 Hola Mundo!"))
asyncio.run( my_client3.send_message_queue("Client Queue 7 Hola Mundo!"))

asyncio.run( my_client4.send_message_topic("Client Topic 4 Hola Mundo!"))
asyncio.run( my_client4.send_message_topic("Client Topic 5 Hola Mundo!"))
asyncio.run( my_client4.send_message_topic("Client Topic 6 Hola Mundo!"))
asyncio.run( my_client4.send_message_topic("Client Topic 7 Hola Mundo!"))

