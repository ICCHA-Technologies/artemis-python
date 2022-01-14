#!/usr/bin/env python

"""
Sample Python connect script. Requires stomp.py: pip install stomp.py
"""

import logging
from time import sleep

import stomp

# NETWORK_RAIL_AUTH = ('username', 'password')
NETWORK_RAIL_AUTH = ('admin', 'admin')

console = logging.StreamHandler()
console.setFormatter(logging.Formatter('[%(asctime)s] %(name)-12s %(levelname)-8s %(message)s'))
logging.getLogger().addHandler(console)
logging.getLogger().setLevel(logging.DEBUG)
LOGGER = logging.getLogger('vstp')


class Listener(stomp.ConnectionListener):

    def __init__(self, mq):
        self._mq = mq

    def on_message(self, headers, message):
        LOGGER.info(headers)
        LOGGER.info(message)
        self._mq.ack(id=headers['message-id'], subscription=headers['subscription'])

    def on_receiver_loop_completed(self,frame):
        print(f'Receiver Loop completed')

    def on_disconnected(self,frame):
        print(f'Desconnected sucessfully')

# mq = stomp.Connection(host_and_ports=[('datafeeds.networkrail.co.uk', 61618)],
#                       keepalive=True,
#                       vhost='datafeeds.networkrail.co.uk',
#                       heartbeats=(5000, 5000))

# mq.set_listener('', Listener(mq))

mq = stomp.Connection()
mq.set_listener('', Listener(mq))



# mq.start()
mq.connect(username=NETWORK_RAIL_AUTH[0],
           passcode=NETWORK_RAIL_AUTH[1],
           wait=True)

mq.subscribe(destination='/queue/test', id=1, ack='auto')
# mq.subscribe('/topic/VSTP_ALL', 'test-vstp', ack='client-individual')

while mq.is_connected():
    sleep(1)