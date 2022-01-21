import logging
import time
import stomp
import sys
from debug import Debugin
import configparser

class Services():
    
    CONSUME_EVENT = '/queue/channel'
    LISTEN_EVENT = '/topic/channel'

    def __init__(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.read('settings/config.ini')

            self.conn = stomp.Connection([(self.config.get('CLIENT','HOST'), self.config.get('CLIENT','PORT'))])
            self.conn.connect(self.config.get('CLIENT','USERNAME'), self.config.get('CLIENT','PASSWORD'), wait=True)

            self.conn.ack(id="1", subscription="1")
            self.conn.set_listener('',self)
        
            if self.config.get('APP','DEBUG')=='True':
                Debugin()
        except stomp.exception.StompException as e:                   
            print(f"Error {e}")

    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_send(self, frame):        
        print(f"Headers: {frame.headers}")
        print('Send a message: "%s"' % frame.body)

    def on_message(self, frame):        
        print(f"Headers: {frame.headers}")
        print('Received a message: "%s"' % frame.body)

    def on_receipt(self, frame):        
        print(f"Headers: {frame.headers}")
        print('On receipt: "%s"' % frame.body)

    def on_receiver_loop_completed():        
        print('On receiver loop completed: "%s"')

    def on_send(self, frame): 
        print(f"Headers: {frame.headers}")
        print('On send: "%s"' % frame.body)
  
    def on_disconnecting(self):
        print('disconnecting')
        print(f"Headers: {frame.headers}")
        connect_and_subscribe(self.conn)

    def on_disconnected(self):
        print('disconnected')
        print(f"Headers: {frame.headers}")
        connect_and_subscribe(self.conn)

    def on_connecting(self,frame):
        print('on_connecting')

    def on_connected(self,frame):
        print('on_connected')
        print('On connected: "%s"' % frame.headers)

    def desconect(self):
        self.conn.disconnect()
        print("Disconected")

    def get_all_queue_messages(self):
        self.conn.subscribe(destination=self.CONSUME_EVENT, id=2, ack='client')
    def get_all_topic_message(self):
        self.conn.subscribe(destination=self.LISTEN_EVENT, id=1, ack='client')

myservices=Services()

while True:
    myservices.get_all_queue_messages()
    time.sleep(3)
    myservices.get_all_topic_message()
    time.sleep(3)
