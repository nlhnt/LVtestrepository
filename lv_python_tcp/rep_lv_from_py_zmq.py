# http://labview-zmq.sourceforge.net/
# https://stackoverflow.com/questions/41009900/python-zmq-operation-cannot-be-accomplished-in-current-state
# https://zeromq.org/languages/python/
# https://pythonspeed.com/articles/docker-connection-refused/
#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6340")

i = 0
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    # time.sleep(1)

    #  Send reply back to client
    socket.send(bytes(f"Python: {i}", 'utf-8'))
    i += 1