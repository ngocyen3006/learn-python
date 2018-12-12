'''
Minh họa hai luồng chạy bất đồng bộ với phương thức print_time()
Vòng lặp của main thread kết thúc khi hai luồng kết thúc
Đây là kỹ thuật cũ (thư viện _thread)
'''
import _thread
import time

dem = 0


# Define a function for the thread


def print_time(threadName, delay):
    global dem
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s, (%i/5): %s" % (threadName, count, time.ctime(time.time())))
    # kết thúc một thread thì đếm 1
    dem += 1


if __name__ == "__main__":
    # Create two threads as follows
    try:
        # 1. call synchronous (đồng bộ)
        print_time("Thread-1", 2)
        print_time("Thread-2", 4)
        dem = 2

        # 2. call asynchronous (bất đồng bộ)
        # _thread.start_new_thread(print_time, ("Thread-1", 2))
        # _thread.start_new_thread(print_time, ("Thread-2", 4))
    except:
        print("Error: unable to start thread")
    # main thread
    while True:  # vòng lặp giữ cho chương trình vẫn chạy
        if dem == 2:  # đã kết thúc hai thread
            break
    # Continue main thread
    print("Exiting Main Thread")
