import grpc
import MessageControl_pb2
import MessageControl_pb2_grpc
import os
import json
import uuid

uuid = str()


def getUUID():
    global uuid
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_dir, "config.json")

    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as file:
            config_data = json.load(file)
            uuid = str(config_data.get("uuid"))
            if uuid:
                print(f"UUID found: {uuid}")
                return

    uuid = str(uuid.uuid4())
    config_data = {"uuid": uuid}
    with open(config_file_path, "w") as file:
        json.dump(config_data, file)
        print(f"New UUID generated and stored in config.json: {uuid}")


def run():
    global uuid
    channel = grpc.insecure_channel('localhost:50051')
    stub = MessageControl_pb2_grpc.MessageControlStub(channel)

    while True:
        message = input(
            'Input message (\'fetch\' to fetch messages, \'quit\' to quit): ')

        if message == 'fetch':
            print(
                stub.Fetch(MessageControl_pb2.FetchRequest(UUID=uuid)).Message)
            continue
        if message == 'quit':
            return

        remain = int(input('Input message remaining time: '))
        request = MessageControl_pb2.UploadRequest(UUID=uuid,
                                                   Message=message,
                                                   RemainTime=remain)
        reponse = stub.Upload(request)
        print(reponse.Message)


if __name__ == '__main__':
    getUUID()
    run()