
import logging
import time
import sys

import stomp

import random



class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_send(self, frame):        
        print(frame.headers)
        print('Send a message: "%s"' % frame.body)

    def on_message(self, frame):        
        print(frame.headers)
        print('Received a message: "%s"' % frame.body)

    def on_receipt(self, frame):        
        print(frame.headers)
        print('On receipt: "%s"' % frame.body)

    def on_receiver_loop_completed():        
        print('On receiver loop completed: "%s"')

    def on_send(self, frame): 
        print(frame.headers)
        print('On send: "%s"' % frame.body)
  
    def on_disconnecting(self):
        print('disconnecting')
        print(frame.headers)
        connect_and_subscribe(self.conn)

    def on_disconnected(self):
        print('disconnected')
        print(frame.headers)
        connect_and_subscribe(self.conn)

    def on_connecting(self,frame):
        print('on_connecting')

    def on_connected(self,frame):
        print('on_connected')
        print('On connected: "%s"' % frame.headers)


try:
    # console = logging.StreamHandler()
    # console.setFormatter(logging.Formatter('[%(asctime)s] %(name)-12s %(levelname)-8s %(message)s'))
    # logging.getLogger().addHandler(console)
    # logging.getLogger().setLevel(logging.DEBUG)
    # LOGGER = logging.getLogger('Server Stomp')

    list_id=[]

    conn1 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    conn1.connect('admin', 'admin', wait=True)
    conn1.ack(id="1", subscription="1")
    conn1.set_listener('', MyListener(conn1))

    conn2 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    conn2.connect('admin', 'admin', wait=True)
    conn2.ack(id="2", subscription="2")
    conn2.set_listener('', MyListener(conn2))

    # my_id=random.randint(1,100)        
    # conn1.ack(id=2,subscription=2)
    conn1.subscribe(destination='/queue/test', id=2, ack='client')
    conn2.subscribe(destination='/queue/test', id=4, ack='client')

    # conn1.ack(id=1,subscription=1)
    conn1.subscribe(destination='/topic/test', id=1, ack='client')
    conn2.subscribe(destination='/topic/test', id=3, ack='client')

    time.sleep(10)
    conn1.unsubscribe(1)
    print(f"*****UNSUBSCRIBE ID 1")


    time.sleep(5)
    print(f"*****NEW SUBSCRIBE ID 1")
    conn1.subscribe(destination='/topic/test', id=1, ack='client')

    # time.sleep(5)
    # print(f"*****NEW SUBSCRIBE ID 1")
    # conn1.subscribe(destination='A.B.C.D', id=1, ack='client')

    time.sleep(600)
    conn1.disconnect()
    print("Disconected")


except stomp.exception.StompException as e:
    print(f"Error {e}")