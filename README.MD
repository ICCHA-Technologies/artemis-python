<h1>This app have two scripts</h1>


<h2><br>service.py</br></h2>

This program creates a connection for a host and a specific port, in addition to supplying the credentials necessary to make that connection, this service is maintained in an infinite cycle.

To run it you must use the following command in your console.

 **python service.py**

implements several abstract methods of the Stomp class.

In addition to two methods that process the messages that are received.

<h3><strong>Method get_all_queue_messages
</strong></h3>
Receives all messages sent to the specific queue channel

<hr>
<strong>The output generate is</strong>

    [2022-01-21 07:00:24,155] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '2', 'content-length': '29', 'message-id': '11108191', 'destination': '/queue/channel', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642770024153'}, body='good morning, today is friday'
    Headers: {'subscription': '2', 'content-length': '29', 'message-id': '11108191', 'destination': '/queue/channel', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642770024153'}
    Received a message: "good morning, today is friday"
    Headers: {'destination': '/topic/channel', 'id': 1, 'ack': 'client'}
    On send: ""

<h3><strong>Method get_all_topic_messages</strong></h3>
Receives all messages sent to the specific topic channel

<hr>
<strong>The output generate is</strong>

    2022-01-21 07:00:57,979] stomp.py     DEBUG    Received frame: 'MESSAGE', headers={'subscription': '1', 'content-length': '8', 'message-id': '11108198', 'destination': '/topic/channel', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642770057976'}, body='nice day'
    Headers: {'subscription': '1', 'content-length': '8', 'message-id': '11108198', 'destination': '/topic/channel', 'expires': '0', 'redelivered': 'false', 'priority': '4', 'persistent': 'false', 'timestamp': '1642770057976'}
    Received a message: "nice day"
    Headers: {'destination': '/queue/channel', 'id': 2, 'ack': 'client'}
    On send: ""

<h2><br>client.py</br></h2>


This program receives by parameter the name of the channel to be sent the message and the message in quotation marks.

To run it you must use the following command in your console.

**python client.py '/topic/channel' 'nice day'**

