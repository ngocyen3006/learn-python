'''
Minh họa hai luồng chạy đồng bộ với phương thức print_time()
Các luồng thuộc lớp con myThread kế thừa lớp cha threading.Thread
Phương thức run tự động chạy khi luồng được start
Phương thức join của luồng sẽ tự động chờ đến khi kết thúc luồng 
thì mới cho chạy tiếp lệnh của main thread
Phương thức acquire của luồng thử yêu cầu khóa luồng để chạy đồng bộ (tạm ngưng các luồng khác)
Phương thức release của luồng thử yêu cầu giải phóng khóa cho luồng
Đây là kỹ thuật mới (thư viện threading)
'''
import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        print(self.name + " đã acquire thành công")
        print_time(self.name, self.delay, 5)
        # Free lock to release next thread
        threadLock.release()
        print(self.name + " đã release thành công")
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    count = 0
    while count < counter:
        time.sleep(delay)
        count += 1
        print("%s, (%i/%i): %s" %
              (threadName, count, counter, time.ctime(time.time())))


if __name__ == "__main__":
    threadLock = threading.Lock()
    threads = []
    # Create new threads
    thread1 = myThread(1, "Thread-1", 2)
    thread2 = myThread(2, "Thread-2", 4)
    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)
    # Start new Threads
    for t in threads:
        t.start()
    # Wait for all threads to complete
    for t in threads:
        t.join()
    # Continue main thread
    print("Exiting Main Thread")
