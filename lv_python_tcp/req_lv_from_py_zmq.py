# http://labview-zmq.sourceforge.net/
# https://stackoverflow.com/questions/41009900/python-zmq-operation-cannot-be-accomplished-in-current-state
# https://zeromq.org/languages/python/
# https://pythonspeed.com/articles/docker-connection-refused/
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
# https://stackoverflow.com/questions/56012210/trying-to-connect-to-a-python-socket-inside-a-docker-container-from-host
# When one host: ("tcp://127.0.0.1:6340")
# When from container it might be hard
socket.connect("tcp://172.17.0.2:6340")

#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))