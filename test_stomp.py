# import client
import threading
import asyncio


from client import ClientStomp

my_client1 = ClientStomp()
my_client2 = ClientStomp()
my_client3 = ClientStomp()
my_client4 = ClientStomp()


asyncio.run( my_client1.send_message_queue("Desde el Client Queue 1 Mensaje 1"))
asyncio.run( my_client2.send_message_topic("Desde el Client Topic 1 Mensaje 1"))
asyncio.run( my_client3.send_message_queue("Desde el Client Queue 2 Mensaje 2"))
asyncio.run( my_client4.send_message_topic("Desde el Client Topic 2 Mensaje 2"))
asyncio.run( my_client3.send_message_queue("Desde el Client Queue 3 Mensaje 3"))
asyncio.run( my_client4.send_message_topic("Desde el Client Topic 3 Mensaje 3"))

asyncio.run( my_client3.send_message_queue("Desde el Client Queue 4 Mensaje 4"))
asyncio.run( my_client3.send_message_queue("Desde el Client Queue 5 Mensaje 5"))
asyncio.run( my_client3.send_message_queue("Desde el Client Queue 6 Mensaje 6"))
asyncio.run( my_client3.send_message_queue("Desde el Client Queue 7 Mensaje 7"))

asyncio.run( my_client4.send_message_topic("Desde el Client Topic 4 Mensaje 4"))
asyncio.run( my_client4.send_message_topic("Desde el Client Topic 5 Mensaje 5"))
asyncio.run( my_client4.send_message_topic("Desde el Client Topic 6 Mensaje 6"))
asyncio.run( my_client4.send_message_topic("Desde el Client Topic 7 Mensaje 7"))

