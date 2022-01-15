
import logging
import time
import sys

import stomp

import random

def connect_and_subscribe_queue(conn,id):
    conn.connect('admin', 'admin', wait=True)
    
    #QUEUE
    conn.subscribe(destination='/queue/test', id=id)

def connect_and_subscribe_topic(conn,id):
    conn.connect('admin', 'admin', wait=True)
    #TOPIC
    
    conn.subscribe(destination='A.B.C.D', id=id, ack='client',headers = {'subscription-type': 'MULTICAST',})    



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
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('[%(asctime)s] %(name)-12s %(levelname)-8s %(message)s'))
    logging.getLogger().addHandler(console)
    logging.getLogger().setLevel(logging.DEBUG)
    LOGGER = logging.getLogger('Server Stomp')

    # conn1 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    # listener1 = conn1.set_listener('', MyListener(conn1))

    # conn2 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    # listener2 = conn2.set_listener('', MyListener(conn2))

    # conn3 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    # listener3 = conn3.set_listener('', MyListener(conn3))


    list_id=[]

    conn4 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    conn4.connect('admin', 'admin', wait=True)
    conn4.set_listener('', MyListener(conn4))

    my_id=random.randint(1,100)        
    list_id.append(my_id)
    conn4.subscribe(destination='/queue/test', id=my_id, ack='client')


    my_id=random.randint(1,100)        
    list_id.append(my_id)
    conn4.subscribe(destination='A.B.C.D', id=my_id, ack='client')

    time.sleep(10)
    conn4.unsubscribe(list_id[0])
    print(f"*****UNSUBSCRIBE ID {list_id[0]}")


    time.sleep(5)
    my_id=random.randint(1,100)            
    list_id.append(my_id)
    print(f"*****NEW SUBSCRIBE ID {my_id}")
    conn4.subscribe(destination='/queue/test', id=my_id, ack='client')
    # connect_and_subscribe_topic(conn4,my_id)    

    # import pdb;pdb.set_trace()

    # conn4.received_heartbeat()
    # conn4.set_receipt()
    # conn4.remove_listener()
    # conn4.set_subscribe()
    # conn4.transport()
    # conn4.unsubscribe()
    # conn4.version()
    # conn4.send("Star War")
    # conn4.send_ssl("Hola mundo")

    # conn4.running()    


    # connect_and_subscribe(conn)    
    # connect_and_subscribe_queue(conn1)    
    # connect_and_subscribe_queue(conn3)    
    # connect_and_subscribe_topic(conn2)    
    # connect_and_subscribe_topic(conn4)    

    # connect_and_subscribe_topic(conn1)    
    # connect_and_subscribe_topic(conn2)    
    # connect_and_subscribe_topic(conn3)    
    # connect_and_subscribe_topic(conn4)    


    time.sleep(30)
    # conn1.disconnect()
    # conn2.disconnect()
    # conn3.disconnect()
    conn4.disconnect()
    print("Disconected")


except stomp.exception.StompException as e:
    print(f"Error {e}")