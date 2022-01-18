
import logging
import time
import stomp


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


    list_id=[]

    conn1 = stomp.Connection([('localhost', 61613)], heartbeats=(4000, 4000))
    conn1.connect('admin', 'admin', wait=True)
    conn1.set_listener('', MyListener(conn1))

    # my_id=random.randint(1,100)        
    my_id=2
    conn1.subscribe(destination='/queue/test', id=my_id, ack='client')
    # conn1.ack(id=my_id,subscription=my_id)

    my_id=1
    list_id.append(my_id)
    conn1.subscribe(destination='A.B.C.D', id=my_id, ack='client')
    # conn1.ack(id=my_id,subscription=my_id)

    time.sleep(10)
    conn1.unsubscribe(2)
    print(f"*****UNSUBSCRIBE ID 2")


    time.sleep(5)
    print(f"*****NEW SUBSCRIBE ID 2")
    conn1.subscribe(destination='/queue/test', id=2, ack='client')

    # time.sleep(5)
    # print(f"*****NEW SUBSCRIBE ID 1")
    # conn1.subscribe(destination='A.B.C.D', id=1, ack='client')

    time.sleep(30)
    conn1.disconnect()
    print("Disconected")


except stomp.exception.StompException as e:
    print(f"Error {e}")