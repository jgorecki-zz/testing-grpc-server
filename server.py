import grpc
import digestor_pb2
import digestor_pb2_grpc
from concurrent import futures
import time
import hashlib


class DigestorServicer(digestor_pb2_grpc.DigestorServicer):
    def __init__(self, *args, **kwargs):
        self.server_port = 46001

    def GetDigestor(self, request, context):

        to_be_digested = request.ToDigest

        digested = to_be_digested

        print(digested)

        result = {'Digested': digested, 'WasDigested': True, 'DigestThis': 'I am an field in the response'}

        print(result)

        return digestor_pb2.DigestedMessage(**result)

    def start_server(self):
        """
        Function which actually starts the gRPC server, and preps
        it for serving incoming connections
        """
        # declare a server object with desired number
        # of thread pool workers.
        digestor_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # This line can be ignored
        digestor_pb2_grpc.add_DigestorServicer_to_server(DigestorServicer(), digestor_server)

        # bind the server to the port defined above
        digestor_server.add_insecure_port('[::]:{}'.format(self.server_port))

        # start the server
        digestor_server.start()
        print('Digestor Server running ...')

        try:
            # need an infinite loop since the above
            # code is non blocking, and if I don't do this
            # the program will exit
            while True:
                time.sleep(60 * 60 * 60)
        except KeyboardInterrupt:
            digestor_server.stop(0)
            print('Digestor Server Stopped ...')

curr_server = DigestorServicer()
curr_server.start_server()



