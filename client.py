import socket
from threading import Thread


class Client:
    server_info = ('127.0.0.1', 8081)

    def __init__(self):
        # socket.AF_INET : IPv4 체계, SOCK_STREAM : TCP 사용
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(self.server_info)

    def receive_thread(self):
        data = self.socket.recv(16)
        print("server : {}".format(data.decode()))

    def send_thread(self):
        while True:
            msg = input()
            self.socket.sendall(msg.encode())

    def run(self):
        # Receive Thread
        Thread(target=self.receive_thread).start()

        # Send Thread
        Thread(target=self.send_thread).start()


if __name__ == '__main__':
    client = Client()
    client.run()
