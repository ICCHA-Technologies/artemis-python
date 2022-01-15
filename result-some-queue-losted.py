[2022-01-14 20:24:35,312] stomp.py     INFO     attempt reconnection (True, None, 0)
[2022-01-14 20:24:35,312] stomp.py     INFO     Attempting connection to host localhost, port 61613
[2022-01-14 20:24:35,312] stomp.py     INFO     Established connection to host localhost, port 61613
[2022-01-14 20:24:35,313] stomp.py     INFO     Starting receiver loop (<Thread(Thread-1, started daemon 139630180771584)>)
[2022-01-14 20:24:35,313] stomp.py     INFO     Created thread <Thread(Thread-1, started daemon 139630180771584)> using func <function default_create_thread at 0x7efe2f9d9790>
[2022-01-14 20:24:35,313] stomp.py     DEBUG    Sending frame: [b'STOMP', b'\n', b'accept-version:1.1\n', b'heart-beat:4000,4000\n', b'login:admin\n', b'passcode:admin\n', b'\n', b'\x00']
[2022-01-14 20:24:35,317] stomp.py     DEBUG    Received frame: 'CONNECTED', headers={'version': '1.1', 'session': '1ceb6ee8', 'server': 'ActiveMQ-Artemis/2.20.0 ActiveMQ Artemis Messaging Engine', 'heart-beat': '4000,4000'}, body=''
[2022-01-14 20:24:35,318] stomp.py     DEBUG    Heartbeats calculated (4000, 4000)
{'destination': '/queue/test', 'id': 95, 'ack': 'client'}
[2022-01-14 20:24:35,318] stomp.py     DEBUG    Set receive_sleep to 6.0, send_sleep to 4.0
On send: ""
[2022-01-14 20:24:35,318] stomp.py     DEBUG    Sending frame: [b'SUBSCRIBE', b'\n', b'ack:client\n', b'destination:/queue/test\n', b'id:95\n', b'\n', b'\x00']
[2022-01-14 20:24:35,318] stomp.py     INFO     Starting heartbeat loop
{'destination': 'A.B.C.D', 'id': 78, 'ack': 'client'}
On send: ""
[2022-01-14 20:24:35,318] stomp.py     DEBUG    Sending frame: [b'SUBSCRIBE', b'\n', b'ack:client\n', b'destination:A.B.C.D\n', b'id:78\n', b'\n', b'\x00']
[2022-01-14 20:24:35,318] stomp.py     DEBUG    Calculated next outbound heartbeat as 127868.378455075
[2022-01-14 20:24:39,318] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:24:39,318] stomp.py     DEBUG    Sending a heartbeat message at 127868.378543064
{}
On send: "None"
[2022-01-14 20:24:39,318] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:24:39,416] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '95', 'content-length': '26', 'message-id': '11101119', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213479415'}, body='Client Queue 1 Hola Mundo!'
{'subscription': '95', 'content-length': '26', 'message-id': '11101119', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213479415'}
Received a message: "Client Queue 1 Hola Mundo!"
[2022-01-14 20:24:41,419] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '78', 'content-length': '26', 'message-id': '11101121', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213481418'}, body='Client Topic 1 Hola Mundo!'
{'subscription': '78', 'content-length': '26', 'message-id': '11101121', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213481418'}
Received a message: "Client Topic 1 Hola Mundo!"
[2022-01-14 20:24:42,426] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '95', 'content-length': '26', 'message-id': '11101123', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213482426'}, body='Client Queue 2 Hola Mundo!'
{'subscription': '95', 'content-length': '26', 'message-id': '11101123', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213482426'}
Received a message: "Client Queue 2 Hola Mundo!"
[2022-01-14 20:24:43,318] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:24:43,319] stomp.py     DEBUG    Sending a heartbeat message at 127872.378771693
{}
On send: "None"
[2022-01-14 20:24:43,319] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:24:44,422] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '78', 'content-length': '26', 'message-id': '11101125', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213484422'}, body='Client Topic 2 Hola Mundo!'
{'subscription': '78', 'content-length': '26', 'message-id': '11101125', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213484422'}
Received a message: "Client Topic 2 Hola Mundo!"
{'id': 95}
On send: ""
[2022-01-14 20:24:45,324] stomp.py     DEBUG    Sending frame: [b'UNSUBSCRIBE', b'\n', b'id:95\n', b'\n', b'\x00']
*****UNSUBSCRIBE ID 95
[2022-01-14 20:24:47,318] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:24:47,427] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '78', 'content-length': '26', 'message-id': '11101141', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213487426'}, body='Client Topic 3 Hola Mundo!'
{'subscription': '78', 'content-length': '26', 'message-id': '11101141', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213487426'}
Received a message: "Client Topic 3 Hola Mundo!"
[2022-01-14 20:24:49,324] stomp.py     DEBUG    Sending a heartbeat message at 127878.384515251
{}
On send: "None"
[2022-01-14 20:24:49,325] stomp.py     DEBUG    Sending frame: [b'\n']
*****NEW SUBSCRIBE ID 34
{'destination': '/queue/test', 'id': 34, 'ack': 'client'}
On send: ""
[2022-01-14 20:24:50,330] stomp.py     DEBUG    Sending frame: [b'SUBSCRIBE', b'\n', b'ack:client\n', b'destination:/queue/test\n', b'id:34\n', b'\n', b'\x00']
[2022-01-14 20:24:50,433] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '34', 'content-length': '26', 'message-id': '11101152', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213490432'}, body='Client Queue 6 Hola Mundo!'
{'subscription': '34', 'content-length': '26', 'message-id': '11101152', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213490432'}
Received a message: "Client Queue 6 Hola Mundo!"
[2022-01-14 20:24:51,318] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:24:51,434] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '34', 'content-length': '26', 'message-id': '11101154', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213491434'}, body='Client Queue 7 Hola Mundo!'
{'subscription': '34', 'content-length': '26', 'message-id': '11101154', 'destination': '/queue/test', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213491434'}
Received a message: "Client Queue 7 Hola Mundo!"
[2022-01-14 20:24:53,440] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '78', 'content-length': '26', 'message-id': '11101156', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213493437'}, body='Client Topic 4 Hola Mundo!'
{'subscription': '78', 'content-length': '26', 'message-id': '11101156', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213493437'}
Received a message: "Client Topic 4 Hola Mundo!"
[2022-01-14 20:24:54,330] stomp.py     DEBUG    Sending a heartbeat message at 127883.390132658
{}
On send: "None"
[2022-01-14 20:24:54,330] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:24:55,318] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:24:55,439] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '78', 'content-length': '26', 'message-id': '11101158', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213495438'}, body='Client Topic 5 Hola Mundo!'
{'subscription': '78', 'content-length': '26', 'message-id': '11101158', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213495438'}
Received a message: "Client Topic 5 Hola Mundo!"
[2022-01-14 20:24:57,442] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '78', 'content-length': '26', 'message-id': '11101160', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213497441'}, body='Client Topic 6 Hola Mundo!'
{'subscription': '78', 'content-length': '26', 'message-id': '11101160', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213497441'}
Received a message: "Client Topic 6 Hola Mundo!"
[2022-01-14 20:24:58,330] stomp.py     DEBUG    Sending a heartbeat message at 127887.390604971
{}
On send: "None"
[2022-01-14 20:24:58,331] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:24:59,319] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:24:59,448] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '78', 'content-length': '26', 'message-id': '11101162', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213499444'}, body='Client Topic 7 Hola Mundo!'
{'subscription': '78', 'content-length': '26', 'message-id': '11101162', 'destination': 'A.B.C.D', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642213499444'}
Received a message: "Client Topic 7 Hola Mundo!"
[2022-01-14 20:25:02,331] stomp.py     DEBUG    Sending a heartbeat message at 127891.390930926
{}
On send: "None"
[2022-01-14 20:25:02,331] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:25:03,318] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:25:06,331] stomp.py     DEBUG    Sending a heartbeat message at 127895.391301147
{}
On send: "None"
[2022-01-14 20:25:06,331] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:25:07,319] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:25:10,331] stomp.py     DEBUG    Sending a heartbeat message at 127899.391636517
{}
On send: "None"
[2022-01-14 20:25:10,332] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:25:11,319] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:25:14,332] stomp.py     DEBUG    Sending a heartbeat message at 127903.392005395
{}
On send: "None"
[2022-01-14 20:25:14,332] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:25:15,319] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
[2022-01-14 20:25:18,332] stomp.py     DEBUG    Sending a heartbeat message at 127907.392593631
{}
On send: "None"
[2022-01-14 20:25:18,333] stomp.py     DEBUG    Sending frame: [b'\n']
[2022-01-14 20:25:19,319] stomp.py     DEBUG    Received frame: 'heartbeat', headers={}, body=None
{'receipt': 'b3174cf5-b4ca-452f-a3a0-02f56e757668'}
On send: ""
[2022-01-14 20:25:20,358] stomp.py     DEBUG    Sending frame: [b'DISCONNECT', b'\n', b'receipt:b3174cf5-b4ca-452f-a3a0-02f56e757668\n', b'\n', b'\x00']
Disconected