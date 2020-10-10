import os
import pingpong_pb2
import pingpong_pb2_grpc
import time
import grpc

print(f"From client {__name__}")


def run():
    counter = 0
    pid = os.getpid()
    with grpc.insecure_channel("localhost:8080") as channel:
        stub = pingpong_pb2_grpc.PingPongServiceStub(channel)
        while True:
            try:
                start = time.time()
                response = stub.ping(pingpong_pb2.Ping(count=counter))
                counter = response.count
                if counter % 1000 == 0:
                    print("%4f : resp=%s : procid=%i" %
                          (time.time() - start, response.count, pid))
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                channel.unsubscribe(close)
                exit()


def close(channel):
    channel.close()


if __name__ == "__main__":
    run()
