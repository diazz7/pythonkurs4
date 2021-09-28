import zmq
import napalm_logs.utils

def socket_messages():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://10.18.10.62:49017')
    socket.setsockopt(zmq.SUBSCRIBE, b'')

    while True:
        raw_objekt = socket.recv()
        yield napalm_logs.utils.unserialize(raw_objekt)

for message in socket_messages():
    if message['ip'] == '10.18.10.72':
        print(message)