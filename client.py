import grpc
import digestor_pb2
import digestor_pb2_grpc


class DigestorClient(object):
    def __init__(self):
        self.host ='localhost'
        self.server_port = 46001
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        self.stub = digestor_pb2_grpc.DigestorStub(self.channel)

    def get_digest(self, message):
        to_digest_message = digestor_pb2.DigestMessage(ToDigest=message)
        return self.stub.GetDigestor(to_digest_message)
