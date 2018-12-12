'''
Minh họa hai luồng chạy bất đồng bộ với phương thức print_time()
Các luồng thuộc lớp con myThread kế thừa lớp cha threading.Thread
Phương thức run tự động chạy khi luồng được start
Phương thức join của luồng sẽ tự động chờ đến khi kết thúc luồng 
thì mới cho chạy tiếp lệnh của main thread
Đây là kỹ thuật mới (thư viện threading)
'''
import threading
import time


# xây dựng lớp myThread kế thừa từ threading.Thread


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.delay, 5)
        print("Exiting " + self.name)


# Define a function for the thread


def print_time(threadName, delay, counter):
    count = 0
    while count < counter:
        time.sleep(delay)
        count += 1
        print("%s, (%i/%i): %s" %
              (threadName, count, counter, time.ctime(time.time())))


if __name__ == "__main__":
    # Create new threads
    thread1 = myThread(threadID=1, name="Thread-1", delay=2)
    thread2 = myThread(threadID=2, name="Thread-2", delay=4)
    # Start new Threads
    thread1.start()
    thread2.start()
    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    # Continue main thread
    print("Exiting Main Thread")
