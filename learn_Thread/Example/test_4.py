import queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)


def process_data(threadName, q):
    global exitFlag
    while not exitFlag:
        # Get lock to synchronize threads
        queueLock.acquire()
        if not q.empty():
            time.sleep(2)
            data = q.get()
            # Free lock to release next thread
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            # Free lock to release next thread
            queueLock.release()
            time.sleep(1)
            exitFlag = 1


if __name__ == "__main__":
    # danh sách tên thread
    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    # dữ liệu gốc
    nameList = ["Zero", "One", "Two", "Three", "Four",
                "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    queueLock = threading.Lock()
    # dữ liệu hàng đợi dành cho các thread xử lý đọc,
    # bảo đảm một thời điểm chỉ có một thread chiếm giữ
    workQueue = queue.Queue(maxsize=20)
    # danh sách thread
    threads = []
    # id các thread bắt đầu từ 1
    threadID = 1

    # Fill the queue
    for word in nameList:
        workQueue.put(word)

    # Create new threads
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    # Wait for all threads to complete
    for t in threads:
        t.join()
    # Continue main thread
    print("Exiting Main Thread")
