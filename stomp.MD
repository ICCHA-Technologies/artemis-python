<H2><b>dir(conn)</b></H2>

['_HeartbeatListener__heartbeat_loop', '_HeartbeatListener__update_heartbeat', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_escape_headers', 'abort', 'ack', 'auto_content_length', 'begin', 'commit', 'connect', 'disconnect', 'disconnecting', 'get_listener', 'get_ssl', 'heart_beat_receive_scale', 'heartbeat_terminate_event', 'heartbeat_thread', 'heartbeats', 'is_connected', 'nack', 'next_outbound_heartbeat', 'on_before_message', 'on_connected', 'on_connecting', 'on_disconnected', 'on_disconnecting', 'on_error', 'on_heartbeat', 'on_heartbeat_timeout', 'on_message', 'on_receipt', 'on_receiver_loop_completed', 'on_send', 'received_heartbeat', 'remove_listener', 'running', 'send', 'send_frame', 'set_listener', 'set_receipt', 'set_ssl', 'subscribe', 'transport', 'unsubscribe', 'version']

<H3><b>conn.abort.__doc__</b></H3>
Abort a transaction.

**param str transaction:** the identifier of the transaction

**param dict headers:** a map of any additional headers the broker requires

**param keyword_headers:** any additional headers the broker requires


<hr>

<H3><b>conn.ack.__doc__</b></H3>

Acknowledge 'consumption' of a message by id. 

**param str id:** identifier of the message

**param str subscription:** the subscription this message is associated with

**param str transaction:** include the acknowledgement in the specified transaction

**param str receipt** the receipt id

<hr>




<H2><b>dir(conn.send)</b></H2>

['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

<H3><b>conn.send.__doc__</b></H3>

Send a message to a destination in the messaging system (as per https://stomp.github.io/stomp-specification-1.2.html#SEND)

**param str destination:** the destination (such as a message queue - for example '/queue/test' - or a message topic)

**param body:** the content of the message.

**param str content_type:** the MIME type of message.

**param dict headers:** additional headers to send in the message frame.

**param keyword_headers:** any additional headers the broker requires.