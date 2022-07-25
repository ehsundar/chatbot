import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(("localhost", 8001))

    sock.sendall(b"1,2,3")

    buf = sock.recv(2000)

    print(buf)


if __name__ == '__main__':
    main()
