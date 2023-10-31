import grpc
import MessageControl_pb2
import MessageControl_pb2_grpc
import os
import json
import uuid

uuid = str()


# 获取UUID，如果已存在则从配置文件中读取，否则生成新的UUID并存储到配置文件中
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


# 运行函数，建立与gRPC服务器的通信，并根据用户输入进行消息的上传和获取
def run():
    global uuid
    channel = grpc.insecure_channel('localhost:50051')  # 创建与gRPC服务器的通信通道
    stub = MessageControl_pb2_grpc.MessageControlStub(channel)  # 创建gRPC客户端存根
    while True:
        message = input(
            'Input message (\'fetch\' to fetch messages, \'quit\' to quit): '
        )  # 用户输入消息内容
        if message == 'fetch':  # 如果输入为'fetch'，则获取消息
            print(
                stub.Fetch(MessageControl_pb2.FetchRequest(
                    UUID=uuid)).Message)  # 调用Fetch方法获取消息
            continue
        if message == 'quit':  # 如果输入为'quit'，则退出程序
            return
        remain = int(input('Input message remaining time: '))  # 用户输入消息的剩余时间
        request = MessageControl_pb2.UploadRequest(
            UUID=uuid, Message=message, RemainTime=remain)  # 构建上传消息的请求对象
        reponse = stub.Upload(request)  # 调用Upload方法上传消息
        print(reponse.Message)  # 打印上传结果


if __name__ == '__main__':
    getUUID()  # 获取或生成UUID
    run()  # 运行程序