import time 
import sys
import stomp
class Listener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
hosts = [('localhost', 61613)] 
conn = stomp.Connection(host_and_ports=hosts)
conn.connect('admin', 'admin', wait=True)
conn.set_listener('', Listener())
# conn.start()
# Register a subscriber with ActiveMQ. This tells ActiveMQ to send
# all messages received on the topic 'topic-1' to this listener
conn.subscribe(destination='/topic/topic-1', id=1, ack='auto') 
# Act as a message publisher and send a message the queue queue-1
conn.send(body=' '.join(sys.argv[1:]), destination='/topic/topic-1')
time.sleep(2)
conn.disconnect()