
import logging
import time
import sys

import stomp


def connect_and_subscribe_queue(conn):
    conn.connect('admin', 'admin', wait=True)
    
    #QUEUE
    conn.subscribe(destination='/queue/test', id=1)

def connect_and_subscribe_topic(conn):
    conn.connect('admin', 'admin', wait=True)
    #TOPIC
    conn.subscribe(destination='A.B.C.D', id=1, ack='client',headers = {'subscription-type': 'MULTICAST',})    



class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_send(self, frame):        
        print('Send a message: "%s"' % frame.body)

    def on_message(self, frame):        
        print(frame.headers)
        print('Received a message: "%s"' % frame.body)

    def on_disconnected(self):
        print('disconnected')
        connect_and_subscribe(self.conn)

try:
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('[%(asctime)s] %(name)-12s %(levelname)-8s %(message)s'))
    logging.getLogger().addHandler(console)
    logging.getLogger().setLevel(logging.DEBUG)
    LOGGER = logging.getLogger('Server Stomp')

    conn1 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    listener1 = conn1.set_listener('', MyListener(conn1))

    conn2 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    listener2 = conn2.set_listener('', MyListener(conn2))

    conn3 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    listener3 = conn3.set_listener('', MyListener(conn3))

    conn4 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    listener4 = conn4.set_listener('', MyListener(conn4))

    # connect_and_subscribe(conn)    
    connect_and_subscribe_queue(conn1)    
    connect_and_subscribe_queue(conn3)    
    connect_and_subscribe_topic(conn2)    
    connect_and_subscribe_topic(conn4)    

    # connect_and_subscribe_topic(conn1)    
    # connect_and_subscribe_topic(conn2)    
    # connect_and_subscribe_topic(conn3)    
    # connect_and_subscribe_topic(conn4)    


    time.sleep(600)
    conn1.disconnect()
    conn2.disconnect()
    conn3.disconnect()
    conn4.disconnect()

except stomp.exception.StompException as e:
    print(f"Error {e}")