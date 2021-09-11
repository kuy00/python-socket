import socket
from threading import Thread


class Server:
    server_info = ('127.0.0.1', 8081)

    def __init__(self):
        # socket.AF_INET : IPv4 체계, SOCK_STREAM : TCP 사용
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.server_info)
        self.client_info = {}

        # 연결 대기
        self.socket.listen()

    def receive_thread(self):
        while True:
            try:
                data = self.client_info['socket'].recv(1024)
                print("client : {}".format(data.decode()))
            except ConnectionResetError as e:
                print('disconnection client : {}'.format(self.client_info['address']))
                break

        self.client_info['socket'].close()

    def send_thread(self):
        while True:
            try:
                msg = input()
                self.client_info['socket'].sendall(msg.encode())
            except ConnectionResetError as e:
                print('disconnection client : {}'.format(self.client_info['address']))
                break

        self.client_info['socket'].close()

    def accept(self):
        # 소켓 접속
        (client_socket, (ip, port)) = self.socket.accept()
        print('connection client : {}'.format((ip, port)))
        self.client_info['socket'] = client_socket
        self.client_info['address'] = {
            'ip': ip,
            'port': port
        }

        # Receive Thread
        Thread(target=self.receive_thread).start()

        # Send Thread
        Thread(target=self.send_thread).start()


if __name__ == '__main__':
    server = Server()

    while True:
        server.accept()
