[2022-01-14 20:21:46,513] stomp.py     INFO     attempt reconnection (True, None, 0)
[2022-01-14 20:21:46,513] stomp.py     INFO     Attempting connection to host localhost, port 61613
[2022-01-14 20:21:46,514] stomp.py     INFO     Established connection to host localhost, port 61613
[2022-01-14 20:21:46,514] stomp.py     INFO     Starting receiver loop (<Thread(Thread-1, started daemon 140615455495936)>)
[2022-01-14 20:21:46,515] stomp.py     INFO     Created thread <Thread(Thread-1, started daemon 140615455495936)> using func <function default_create_thread at 0x7fe39690c790>
[2022-01-14 20:21:46,515] stomp.py     DEBUG    Sending frame: [b'STOMP', b'\n', b'accept-version:1.1\n', b'heart-beat:4000,4000\n', b'login:admin\n', b'passcode:admin\n', b'\n', b'\x00']
[2022-01-14 20:21:46,520] stomp.py     DEBUG    Received frame: 'CONNECTED', headers={'version': '1.1', 'session': '4edac181', 'server': 'ActiveMQ-Artemis/2.20.0 ActiveMQ Artemis Messaging Engine', 'heart-beat': '4000,4000'}, body=''
[2022-01-14 20:21:46,520] stomp.py     DEBUG    Heartbeats calculated (4000, 4000)
[2022-01-14 20:21:46,520] stomp.py     DEBUG    Set receive_sleep to 6.0, send_sleep to 4.0
[2022-01-14 20:21:46,520] stomp.py     INFO     Starting heartbeat loop
{'destination': '/queue/test', 'id': 92, 'ack': 'client'}
[2022-01-14 20:21:46,521] stomp.py     DEBUG    Calculated next outbound heartbeat as 127699.580870728
On send: ""
[2022-01-14 20:21:46,521] stomp.py     DEBUG    Sending frame: [b'SUBSCRIBE', b'\n', b'ack:client\n', b'destination:/queue/test\n', b'id:92\n', b'\n', b'\x00']
{'destination': 'A.B.C.D', 'id': 92, 'ack': 'client'}
On send: ""
[2022-01-14 20:21:46,521] stomp.py     DEBUG    Sending frame: [b'SUBSCRIBE', b'\n', b'ack:client\n', b'destination:A.B.C.D\n', b'id:92\n', b'\n', b'\x00']
[2022-01-14 20:21:46,527] stomp.py     DEBUG    Received frame: 'ERROR', headers={'message': 'There already is a subscription for: 92. Either use unique subscription IDs or do not create multiple subscriptions for the same destination'}, body=''
received an error ""
[2022-01-14 20:21:49,292] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '92', 'content-length': '26', 'message-id': '11101028', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213309291'}, body='Client Queue 1 Hola Mundo!'
{'subscription': '92', 'content-length': '26', 'message-id': '11101028', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213309291'}
Received a message: "Client Queue 1 Hola Mundo!"
[2022-01-14 20:21:50,521] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:21:50,521] stomp.py     DEBUG    Sending a heartbeat message at 127699.581339585
{}
On send: "None"
[2022-01-14 20:21:50,521] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:21:52,304] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '92', 'content-length': '26', 'message-id': '11101032', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213312296'}, body='Client Queue 2 Hola Mundo!'
{'subscription': '92', 'content-length': '26', 'message-id': '11101032', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213312296'}
Received a message: "Client Queue 2 Hola Mundo!"
[2022-01-14 20:21:54,520] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:21:54,521] stomp.py     DEBUG    Sending a heartbeat message at 127703.58156027
{}
On send: "None"
[2022-01-14 20:21:54,521] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:21:55,301] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '92', 'content-length': '26', 'message-id': '11101036', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213315300'}, body='Client Queue 3 Hola Mundo!'
{'subscription': '92', 'content-length': '26', 'message-id': '11101036', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213315300'}
Received a message: "Client Queue 3 Hola Mundo!"
{'id': 92}
On send: ""
[2022-01-14 20:21:56,525] stomp.py     DEBUG    Sending frame: [b'UNSUBSCRIBE', b'\n', b'id:92\n', b'\n', b'\x00']
*****UNSUBSCRIBE ID 92
[2022-01-14 20:21:58,520] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:22:00,525] stomp.py     DEBUG    Sending a heartbeat message at 127709.585147263
{}
On send: "None"
[2022-01-14 20:22:00,525] stomp.py     DEBUG    Sending frame: [b'\n']
*****NEW SUBSCRIBE ID 2
{'destination': '/queue/test', 'id': 2, 'ack': 'client'}
On send: ""
[2022-01-14 20:22:01,530] stomp.py     DEBUG    Sending frame: [b'SUBSCRIBE', b'\n', b'ack:client\n', b'destination:/queue/test\n', b'id:2\n', b'\n', b'\x00']
[2022-01-14 20:22:02,520] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:22:05,530] stomp.py     DEBUG    Sending a heartbeat message at 127714.590692683
{}
On send: "None"
[2022-01-14 20:22:05,531] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:22:06,521] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:22:09,531] stomp.py     DEBUG    Sending a heartbeat message at 127718.591032184
{}
On send: "None"
[2022-01-14 20:22:09,531] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:22:10,521] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:22:13,531] stomp.py     DEBUG    Sending a heartbeat message at 127722.591647281
{}
On send: "None"
[2022-01-14 20:22:13,532] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:22:14,521] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:22:17,532] stomp.py     DEBUG    Sending a heartbeat message at 127726.592036516
{}
On send: "None"
[2022-01-14 20:22:17,532] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:22:18,521] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:22:21,532] stomp.py     DEBUG    Sending a heartbeat message at 127730.592481359
{}
On send: "None"
[2022-01-14 20:22:21,532] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:22:22,522] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:22:25,533] stomp.py     DEBUG    Sending a heartbeat message at 127734.592870234
{}
On send: "None"
[2022-01-14 20:22:25,533] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:22:26,522] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:22:29,533] stomp.py     DEBUG    Sending a heartbeat message at 127738.5933172
{}
On send: "None"
[2022-01-14 20:22:29,533] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:22:30,522] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
{'receipt': '501e7dce-df0e-4e81-b730-901659959c98'}
On send: ""
[2022-01-14 20:22:31,544] stomp.py     DEBUG    Sending frame: [b'DISCONNECT', b'\n', b'receipt:501e7dce-df0e-4e81-b730-901659959c98\n', b'\n', b'\x00']
Disconected