import logging
import time
import stomp

class Services():
    def __init__(self):
        try:
            self.conn1 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))           
            self.conn1.connect('admin', 'admin', wait=True)
            self.conn1.ack(id="1", subscription="1")
            self.conn1.set_listener('',self)

        except stomp.exception.StompException as e:
            print(f"Error {e}")

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

    def desconect(self):
        self.conn1.disconnect()
        print("Disconected")

    def get_all_queue_messages(self):
        self.conn1.subscribe(destination='/queue/test', id=2, ack='client')
    def get_all_topic_message(self):
        self.conn1.subscribe(destination='/topic/test', id=1, ack='client')

myservices=Services()
while True:
    myservices.get_all_queue_messages()
    time.sleep(3)
    myservices.get_all_topic_message()
    time.sleep(3)
