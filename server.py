from concurrent import futures
import grpc
import pingpong_pb2
import pingpong_pb2_grpc
import time
import threading


class Listener(pingpong_pb2_grpc.PingPongServiceServicer):
    def __init__(self, *args, **kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()

    def ping(self, request, context):
        self.counter += 1
        if self.counter > 10000:
            print("10000 calls in %3f seconds" %
                  (time.time() - self.lastPrintTime))
            self.lastPrintTime = time.time()
            self.counter = 0
        return pingpong_pb2.Pong(count=request.count + 1)
