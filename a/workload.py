import threading
import time


def workload(name: str, duration: int):
    for i in range(duration):
        print(f"from thread {threading.current_thread().ident} - {name}: Hello!", flush=True)
        for j in range(1000000):
            a = 1+2


def main():
    threads = []
    for i in range(100):
        th = threading.Thread(target=workload, args=(f"thread-amir-{i}", 100), name=f"thread-amir-{i}")
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


if __name__ == '__main__':
    main()
