import socket


def main():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.bind(("localhost", 8001))
            sock.listen()

            conn, addr = sock.accept()
            with conn:
                buf = conn.recv(2000)
                print(buf)

                payload = buf.decode()

                items = payload.split(",")
                items_int = map(int, items)

                resp = sum(items_int)

                conn.send(str(resp).encode())

        except KeyboardInterrupt:
            print("exiting")
            break


if __name__ == '__main__':
    main()
