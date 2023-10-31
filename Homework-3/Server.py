import grpc
import MessageControl_pb2
import MessageControl_pb2_grpc
from concurrent import futures
import time
import datetime


# 定义MessageControlServicer类，用于实现gRPC服务端的逻辑
class MessageControlServicer(MessageControl_pb2_grpc.MessageControlServicer):

    def __init__(self):
        self.MessagePool = dict()  # 存储消息的字典，以UUID为键，消息列表为值

    # 实现Upload方法，用于上传消息
    def Upload(self, Request, Context):
        uuid, Message, RemainTime = Request.UUID, Request.Message, Request.RemainTime
        if uuid not in self.MessagePool:  # 如果UUID不在消息池中，添加一个空的消息列表
            self.MessagePool[uuid] = []
        timestamp = int(time.time())  # 获取当前时间戳
        self.MessagePool[uuid].append(
            (timestamp + RemainTime, Message))  # 将消息添加到对应的消息列表中
        return MessageControl_pb2.UploadResponse(
            Message=f'{uuid}\'s message successfully uploaded!')

    # 实现Fetch方法，用于获取消息
    def Fetch(self, Request, Context):
        uuid = Request.UUID
        if uuid not in self.MessagePool or len(
                self.MessagePool[uuid]) == 0:  # 如果UUID不在消息池中或者消息列表为空，返回相应的提示信息
            return MessageControl_pb2.FetchResponse(
                Message=f'{uuid} have no messages')
        context = f'{uuid} have messages belowing:'
        self.Fresh(uuid)  # 调用Fresh方法，清除过期的消息
        for it in range(len(self.MessagePool[uuid])):  # 遍历消息列表，构建返回的消息内容
            context += f'\nMessage {it}: {self.MessagePool[uuid][it][1]}\nDeadtime:  {datetime.datetime.fromtimestamp(self.MessagePool[uuid][it][0]).strftime("%Y-%m-%d %H:%M:%S")}'
        return MessageControl_pb2.FetchResponse(Message=context)

    # 实现Fresh方法，用于清除过期的消息
    def Fresh(self, uuid):
        timestamp = int(time.time())  # 获取当前时间戳
        self.MessagePool[uuid].sort(reverse=True)  # 按照消息的过期时间进行排序（降序）
        counter = 0
        while len(self.MessagePool[uuid]) != 0 and self.MessagePool[uuid][-1][
                0] < timestamp:  # 当消息列表不为空且最后一条消息的过期时间小于当前时间戳时，删除该消息
            self.MessagePool[uuid].pop()
            counter += 1
        if counter != 0:
            print(
                f'Delete {counter} outdated messages of {uuid}')  # 打印删除过期消息的数量
        return


# 定义serve函数，用于启动gRPC服务器
def serve():
    server = grpc.server(futures.ThreadPoolExecutor())  # 创建gRPC服务器
    Handler = MessageControlServicer()  # 创建MessageControlServicer实例
    MessageControl_pb2_grpc.add_MessageControlServicer_to_server(
        Handler, server)  # 将MessageControlServicer注册到服务器中
    server.add_insecure_port('[::]:50051')  # 指定服务器监听的端口
    server.start()  # 启动服务器
    print('Waiting for requests...')
    server.wait_for_termination()  # 等待请求的到来并处理


if __name__ == '__main__':
    serve()  # 启动服务器